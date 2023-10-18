# distutils: language = c++
# cython: language_level = 3
from libcpp.string cimport string
from libcpp.vector cimport vector
from libcpp.map cimport map, pair
from libcpp cimport bool

from cython.operator cimport dereference
from cytools cimport env, enc, penc, pdec, map_to_dict
from cyoptimizer cimport CyOptimizer, CyEpoch, CheckDifference
from cytypes cimport folds_t, data_t, metric_t

from AnalysisG._cmodules.cPlots import MetricPlots
import numpy as np

from torch_geometric.data import Batch
import psutil
import torch
import h5py
import pickle

cdef dict fetch_data(list inpt, map[string, k_graphed*]* gr, bar, str device):
    cdef int i
    cdef k_graphed* gx
    cdef dict output = {}
    for i in range(len(inpt)):
        if not inpt[i].Graph: continue
        x = inpt[i].release_graph()
        x = x.to("cpu", non_blocking = True)
        output[inpt[i].hash] = x.to(device, non_blocking = True)
        gx = dereference(gr)[enc(inpt[i].hash)]
        gx.pkl = pickle.dumps(x)
        gx.online = True
        bar.update(1)
    return output


cdef void _check_h5(f, str key, data_t* inpt):
    f.create_dataset(key + "-truth"   , data = np.array(inpt.truth),    chunks = True)
    f.create_dataset(key + "-pred"    , data = np.array(inpt.pred) ,    chunks = True)
    f.create_dataset(key + "-index"   , data = np.array(inpt.index),    chunks = True)
    f.create_dataset(key + "-nodes"   , data = np.array(inpt.nodes),    chunks = True)
    f.create_dataset(key + "-loss"    , data = np.array(inpt.loss) ,    chunks = True)
    f.create_dataset(key + "-accuracy", data = np.array(inpt.accuracy), chunks = True)

cdef void _rebuild_h5(f, str key, data_t* inpt):
    x = np.zeros(f[key + "-truth"].shape)
    f[key + "-truth"].read_direct(x)
    inpt.truth    = <vector[vector[float]]>x.tolist()

    x = np.zeros(f[key + "-pred"].shape)
    f[key + "-pred"].read_direct(x)
    inpt.pred    = <vector[vector[float]]>x.tolist()

    x = np.zeros(f[key + "-index"].shape)
    f[key + "-index"].read_direct(x)
    inpt.index    = <vector[vector[float]]>x.tolist()

    x = np.zeros(f[key + "-nodes"].shape)
    f[key + "-nodes"].read_direct(x)
    inpt.nodes    = <vector[vector[float]]>x.tolist()

    x = np.zeros(f[key + "-loss"].shape)
    f[key + "-loss"].read_direct(x)
    inpt.loss    = <vector[vector[float]]>x.tolist()

    x = np.zeros(f[key + "-accuracy"].shape)
    f[key + "-accuracy"].read_direct(x)
    inpt.accuracy    = <vector[vector[float]]>x.tolist()


def _check_sub(f, str key):
    try: return f.create_group(key)
    except ValueError: return f[key]

cdef struct k_graphed:
    string pkl
    bool online

cdef class cOptimizer:
    cdef CyOptimizer* ptr
    cdef dict _kModel
    cdef dict _kOptim
    cdef bool _train
    cdef bool _test
    cdef bool _val

    cdef dict online_
    cdef map[string, k_graphed] graphs_
    cdef vector[string] cached_
    cdef public metric_plot

    def __cinit__(self):
        self.ptr = new CyOptimizer()
        self._train = False
        self._test  = False
        self._val   = False
        self.online_ = {}

        self.metric_plot = MetricPlots()

    def __init__(self): pass
    def __dealloc__(self): del self.ptr
    def length(self): return map_to_dict(<map[string, int]>self.ptr.fold_map())

    @property
    def kFolds(self): return self.ptr.use_folds

    def GetHDF5Hashes(self, str path) -> bool:
        if path.endswith(".hdf5"): pass
        else: path += ".hdf5"

        try: f = h5py.File(path, "r")
        except FileNotFoundError: return False

        cdef str hash_, key_
        cdef folds_t fold_hash

        for hash_ in f:
            fold_hash = folds_t()
            fold_hash.event_hash = enc(hash_)
            try:
                fold_hash.test = f[hash_].attrs["test"]
                self.ptr.register_fold(&fold_hash)
                continue
            except KeyError: fold_hash.test = False

            try: f[hash_].attrs["train"]
            except KeyError: continue
            for key_ in f[hash_].attrs:
                if not key_.startswith("k-"): continue
                fold_hash.kfold = int(key_[2:])
                fold_hash.train = f[hash_].attrs[key_]
                if fold_hash.train: pass
                else: fold_hash.evaluation = True
                self.ptr.register_fold(&fold_hash)
        return True

    def UseAllHashes(self, dict inpt):
        cdef str key, hash_
        cdef dict data = inpt["graph"]
        cdef folds_t fold_hash
        for key in data:
            for hash_ in data[key]:
                fold_hash = folds_t()
                fold_hash.kfold = 1
                fold_hash.train = True
                fold_hash.event_hash = enc(hash_)
                self.ptr.register_fold(&fold_hash)
            data[key] = None

    cpdef MakeBatch(self, sampletracer, vector[string] batch, int kfold):
        cdef string x
        cdef tuple cuda
        cdef vector[string] lst_

        if   self._train: lst_ = self.ptr.check_train(&batch, kfold)
        elif   self._val: lst_ = self.ptr.check_validation(&batch, kfold)
        elif  self._test: lst_ = self.ptr.check_evaluation(&batch)
        if not lst_.size(): return Batch().from_data_list([self.online_[env(x)] for x in batch])
        self.frost([lst_], batch.size(), sampletracer)

        if len(sampletracer.MonitorMemory("Graph")):
            if  self._train: self.ptr.flush_train(&lst_, kfold)
            elif  self._val: self.ptr.flush_validation(&lst_, kfold)
            elif self._test: self.ptr.flush_evaluation(&lst_)
            self.FlushRunningCache(True)

        if sampletracer.MaxGPU != -1: pass
        else: return Batch().from_data_list([self.online_[env(x)] for x in batch])

        cuda = torch.cuda.mem_get_info()
        if (cuda[1] - cuda[0])/(1024**3) > sampletracer.MaxGPU:
            self.FlushRunningCache(True)
            torch.cuda.empty_cache()

        return Batch().from_data_list([self.online_[env(x)] for x in batch])

    cpdef frost(self, vector[vector[string]] inpt, int batch_size, sampletracer):

        cdef vector[string] itx, full
        for itx in inpt: full.insert(full.end(), itx.begin(), itx.end())

        cdef list fetch = []
        cdef pair[string, int] itm_
        cdef map[string, int] itm = CheckDifference(full, self.cached_, sampletracer.Threads)

        cdef k_graphed* gr
        cdef map[string, k_graphed*] tmp
        for itm_ in itm:
            gr = &self.graphs_[itm_.first]
            if itm_.second and gr.online: continue
            elif itm_.second and not gr.online:
                self.online_[itm_.second] = pickle.loads(gr.pkl).to(sampletracer.Device)
                gr.online = True
                continue
            self.cached_.push_back(itm_.first)
            fetch.append(env(itm_.first))
            tmp[itm_.first] = gr

        if not len(fetch): return
        sampletracer.RestoreGraphs(fetch)
        _, bar = sampletracer._makebar(len(fetch), "Transferring Graphs to " + sampletracer.Device)
        fetch = sampletracer[fetch] if inpt.size() > 1 else [sampletracer[fetch]]
        cdef dict load = fetch_data(fetch, &tmp, bar, sampletracer.Device)
        self.online_.update(load)
        del bar

    def FetchTraining(self, int kfold, int batch_size):
        self._train = True
        self._test  = False
        self._val   = False
        return self.ptr.fetch_train(kfold, batch_size)

    def FetchValidation(self, int kfold, int batch_size):
        self._train = False
        self._test  = False
        self._val   = True
        return self.ptr.fetch_validation(kfold, batch_size)

    def FetchEvaluation(self, int batch_size):
        self._train = False
        self._test  = True
        self._val   = False
        return self.ptr.fetch_evaluation(batch_size)

    def UseTheseFolds(self, list inpt): self.ptr.use_folds = <vector[int]>inpt

    cdef void FlushRunningCache(self, bool flush):
        if not flush: return
        cdef string x
        cdef int index = int(len(self.online_)*0.1)
        for x, i in self.online_.items():
            self.graphs_[x].online = False
            del i
            if index == 0: break
            index -= 1

    cdef void convert(self, ten, vector[vector[float]]* app):
        if len(ten.size()) == 0: ten = ten.view(-1, 1)
        else: ten = ten.view(ten.size()[0], -1)
        cdef vector[vector[float]] it = <vector[vector[float]]>ten.tolist()
        app.insert(app.end(), it.begin(), it.end())

    cdef void makegraph(self, dict graph, map[string, data_t]* app, dict out_map):
        cdef str key, val
        cdef pair[string, data_t] itr
        for key, val in out_map.items():

            try: ten = graph[val]
            except KeyError: ten = None
            if ten is None: pass
            else: self.convert(ten, &(dereference(app)[enc(val[2:])].pred))

            try: ten = graph[key]
            except KeyError: ten = None
            if ten is None: pass
            else:
                self.convert(ten, &(dereference(app)[enc(val[2:])].truth))
                ten = torch.full(ten.size(), graph["i"].item())
                self.convert(ten, &(dereference(app)[enc(val[2:])].index))

            try: ten = graph["num_nodes"]
            except KeyError: ten = None
            if ten is None: pass
            else: self.convert(ten, &(dereference(app)[enc(val[2:])].nodes))


    cpdef AddkFold(self, int epoch, int kfold, dict inpt, dict out_map):
        cdef str key, val
        cdef string key_
        cdef map[string, data_t] map_data
        cdef vector[vector[float]]* its
        cdef vector[vector[float]] itt
        for val, key in out_map.items():
            key  = key[2:]
            key_ = enc(key)
            map_data[key_] = data_t()
            map_data[key_].name = key_
            try: ten = inpt["A_" + key]
            except KeyError: ten = None
            if ten is None: pass
            else: self.convert(ten, &(map_data[key_].accuracy))

            try: ten = inpt["L_" + key]
            except KeyError: ten = None
            if ten is None: pass
            else: self.convert(ten, &(map_data[key_].loss))

        cdef int i
        cdef list graphs = inpt.pop("graphs")
        for i in range(len(graphs)):
            self.makegraph(graphs[i].to_dict(), &map_data, out_map)

        if  self._train: self.ptr.train_epoch_kfold(epoch, kfold, &map_data)
        elif self._test: self.ptr.evaluation_epoch_kfold(epoch, kfold, &map_data)
        else: self.ptr.validation_epoch_kfold(epoch, kfold, &map_data)


    cpdef DumpEpochHDF5(self, int epoch, str path, vector[int] kfolds):

        cdef int i
        cdef str out
        cdef CyEpoch* ep
        cdef pair[string, data_t] dt
        for i in kfolds:
            out = path + str(i) + "/epoch_data.hdf5"
            try: f = h5py.File(out, "w")
            except FileNotFoundError: return False
            if self.ptr.epoch_train.count(epoch):
                grp = _check_sub(f, "training")
                ep = self.ptr.epoch_train[epoch]
                for dt in ep.container[i]:
                    ref = _check_h5(grp, env(dt.first), &dt.second)

            if self.ptr.epoch_valid.count(epoch):
                grp = _check_sub(f, "validation")
                ep = self.ptr.epoch_valid[epoch]
                for dt in ep.container[i]:
                    ref = _check_h5(grp, env(dt.first), &dt.second)

            if self.ptr.epoch_test.count(epoch):
                grp = _check_sub(f, "evaluation")
                ep = self.ptr.epoch_test[epoch]
                for dt in ep.container[i]:
                    ref = _check_h5(grp, env(dt.first), &dt.second)
            f.close()


    cpdef RebuildEpochHDF5(self, int epoch, str path, int kfold):
        cdef str get = path + str(kfold) + "/epoch_data.hdf5"
        try: f = h5py.File(get, "r")
        except FileNotFoundError: return

        cdef str key
        cdef dict unique = {}
        cdef map[string, data_t] ep_k

        for key in f["training"].keys():
            key = key.split("-")[0]
            if key in unique: pass
            else: unique[key] = None

        for key in unique:
            ep_k[enc(key)] = data_t()
            _rebuild_h5(f["training"], key, &ep_k[enc(key)])
        self.ptr.train_epoch_kfold(epoch, kfold, &ep_k)
        ep_k.clear()

        for key in unique:
            ep_k[enc(key)] = data_t()
            _rebuild_h5(f["validation"], key, &ep_k[enc(key)])
        self.ptr.validation_epoch_kfold(epoch, kfold, &ep_k)
        ep_k.clear()

        for key in unique:
            ep_k[enc(key)] = data_t()
            _rebuild_h5(f["evaluation"], key, &ep_k[enc(key)])

        self.ptr.evaluation_epoch_kfold(epoch, kfold, &ep_k)
        ep_k.clear()
        f.close()


    cpdef BuildPlots(self, int epoch, str path):
        self.metric_plot.epoch = epoch
        self.metric_plot.path = path
        cdef CyEpoch* eptr
        if self.ptr.epoch_train.count(epoch):
            eptr = self.ptr.epoch_train[epoch]
            self.metric_plot.AddMetrics(eptr.metrics(), b'training')
            self.ptr.epoch_train.erase(epoch)
            del eptr

        cdef CyEpoch* epva
        if self.ptr.epoch_valid.count(epoch):
            epva = self.ptr.epoch_valid[epoch]
            self.metric_plot.AddMetrics(epva.metrics(), b'validation')
            self.ptr.epoch_valid.erase(epoch)
            del epva

        cdef CyEpoch* epte
        if self.ptr.epoch_test.count(epoch):
            epte = self.ptr.epoch_test[epoch]
            self.metric_plot.AddMetrics(epte.metrics(), b'evaluation')
            self.ptr.epoch_test.erase(epoch)
            del epte

        self.metric_plot.ReleasePlots(path)


