from libcpp.string cimport string
from libcpp.vector cimport vector
from libcpp.map cimport map, pair
from libcpp cimport bool

from cython.operator cimport dereference
from cytypes cimport code_t, event_t, graph_t, selection_t, export_t

from cyevent cimport CyEventTemplate
from cygraph cimport CyGraphTemplate
from cyselection cimport CySelectionTemplate

import pickle
import h5py

ctypedef fused gen_t:
    int
    bool
    string

ctypedef fused common_t:
    event_t
    graph_t
    selection_t

ctypedef fused obj_t:
    CyEventTemplate
    CyGraphTemplate
    CySelectionTemplate

cdef extern from "../abstractions/abstractions.h" namespace "Tools":
    string encode64(string*) except + nogil
    string decode64(string*) except + nogil
    string Hashing(string) except + nogil

cdef inline string enc(str val): return val.encode("UTF-8")
cdef inline str env(string val): return val.decode("UTF-8")

cdef inline vector[string] penc(list strings):
    cdef str s
    return [s.encode("UTF-8") for s in strings]

cdef inline list pdec(vector[string]* strings):
    cdef string s
    return [s.decode("UTF-8") for s in dereference(strings)]

cdef inline dict _decoder(str inpt):
    cdef string x = enc(inpt)
    return pickle.loads(decode64(&x))

cdef inline string _encoder(inpt):
    cdef string x = pickle.dumps(inpt)
    return encode64(&x)

cdef inline list map_to_list(map[string, gen_t] inpt):
    cdef pair[string, gen_t] its
    cdef list output = []
    for its in inpt: output.append(env(its.first))
    return output

cdef inline dict map_to_dict(map[string, gen_t] inpt):
    cdef pair[string, gen_t] its
    cdef dict output = {}
    for its in inpt:
        if isinstance(its.second, int): output[env(its.first)] = its.second
        else: output[env(its.first)] = its.second.decode("UTF-8")
    return output



cdef inline merge(map[string, vector[string]]* out, map[string, string]* get, string hash_):
    if not get.size(): return
    cdef pair[string, string] itr
    for itr in dereference(get): dereference(out)[itr.first].push_back(hash_)

cdef inline dict map_vector_to_dict(map[string, vector[string]]* inpt):
    cdef pair[string, vector[string]] itr
    cdef string h
    cdef dict output = {}
    for itr in dereference(inpt): output[env(itr.first)] = [env(h) for h in itr.second]
    return output

# ----------------------- cache dumpers -------------------------- #
cdef inline list recast_obj(vector[obj_t*] cont, export_t* exp, string cache_path, string daod):
    cdef string hash_
    cdef map[string, string]* path_
    cdef map[string, vector[string]]* hashes_
    cdef list output = []

    for obj_t in cont:
        hash_ = obj_t.Hash()
        if obj_t.is_event:
            (<CyEventTemplate*>(obj_t)).event.cached = True
            output.append((<CyEventTemplate*>(obj_t)).event)
            hashes_, path_ = &exp.event_name_hash, &exp.event_dir

        elif obj_t.is_graph:
            (<CyGraphTemplate*>(obj_t)).graph.cached = True
            output.append((<CyGraphTemplate*>(obj_t)).Export())
            hashes_, path_ = &exp.graph_name_hash, &exp.graph_dir

        elif obj_t.is_selection:
            (<CySelectionTemplate*>(obj_t)).selection.cached = True
            output.append((<CySelectionTemplate*>(obj_t)).selection)
            hashes_, path_ = &exp.selection_name_hash, &exp.selection_dir

        dereference(hashes_)[daod].push_back(hash_)
        dereference(path_)[daod] = cache_path
    return output

cdef inline save_base(ref, common_t* com):
    ref.attrs["event_name"]    = com.event_name
    ref.attrs["code_hash"]     = com.code_hash
    ref.attrs["event_hash"]    = com.event_hash
    ref.attrs["event_tagging"] = com.event_tagging
    ref.attrs["event_tree"]    = com.event_tree
    ref.attrs["event_root"]    = com.event_root
    ref.attrs["weight"]        = com.weight
    ref.attrs["cached"]        = com.cached
    ref.attrs["pickled_data"]  = encode64(&com.pickled_data)
    ref.attrs["event_index"]   = com.event_index

cdef inline save_event(ref, event_t* ev):
    ev.cached = True
    save_base(ref, ev)
    ref.attrs["commit_hash"] = ev.commit_hash
    ref.attrs["deprecated"]  = ev.deprecated
    ref.attrs["event"]       = ev.event

cdef inline save_graph(ref, graph_t* gr):
    save_base(ref, gr)
    ref.attrs["train"]           = gr.train
    ref.attrs["evaluation"]      = gr.evaluation
    ref.attrs["validation"]      = gr.validation

    ref.attrs["empty_graph"]     = gr.empty_graph
    ref.attrs["skip_graph"]      = gr.skip_graph
    ref.attrs["self_loops"]      = gr.self_loops

    ref.attrs["errors"]          = _encoder(gr.errors)
    ref.attrs["presel"]          = _encoder(gr.presel)
    ref.attrs["src_dst"]         = _encoder(gr.src_dst)
    ref.attrs["hash_particle"]   = _encoder(gr.hash_particle)
    ref.attrs["graph_feature"]   = _encoder(gr.graph_feature)
    ref.attrs["node_feature"]    = _encoder(gr.node_feature)
    ref.attrs["edge_feature"]    = _encoder(gr.edge_feature)
    ref.attrs["pre_sel_feature"] = _encoder(gr.pre_sel_feature)

    ref.attrs["topo_hash"]       = gr.topo_hash
    ref.attrs["graph"]           = gr.graph

cdef inline save_selection(ref, selection_t* sel):
    save_base(ref, sel)

    ref.attrs["errors"]                = _encoder(sel.errors)
    ref.attrs["pickled_strategy_data"] = sel.pickled_strategy_data

    ref.attrs["cutflow"]               = _encoder(sel.cutflow)
    ref.attrs["timestats"]             = sel.timestats
    ref.attrs["all_weights"]           = sel.all_weights
    ref.attrs["selection_weights"]     = sel.selection_weights

    ref.attrs["allow_failure"]         = sel.allow_failure

    ref.attrs["_params_"]              = encode64(&sel._params_)
    ref.attrs["selection"]             = sel.selection

cdef inline tracer_link(f, map[string, vector[string]]* hashes, map[string, string]* dirs, str keys, string root_name):
    cdef string hash_, name_, path_
    cdef pair[string, string] itr

    try: ref_e = f.create_dataset(keys + "_dir", (1), dtype = h5py.ref_dtype)
    except ValueError: ref_e = f[keys + "_dir"]
    for itr in dereference(dirs):
        name_, path_ = itr.first, itr.second
        if name_.rfind(root_name, 0) != 0: continue
        name_ = name_.substr(name_.rfind(b":")+1, name_.size())
        try: ref_h = f.create_dataset(keys + ":" + env(name_), (1), dtype = h5py.ref_dtype)
        except ValueError: ref_h = f[keys + ":" + env(name_)]
        for hash_ in dereference(hashes)[itr.first]: ref_h.attrs[hash_] = root_name
        ref_e.attrs[name_] = path_


cdef inline restore_base(ref, common_t* com):
    com.event_name    = enc(ref.attrs["event_name"])
    com.code_hash     = enc(ref.attrs["code_hash"])
    com.event_hash    = enc(ref.attrs["event_hash"])
    com.event_tagging = enc(ref.attrs["event_tagging"])
    com.event_tree    = enc(ref.attrs["event_tree"])
    com.event_root    = enc(ref.attrs["event_root"])
    com.weight        = ref.attrs["weight"]
    com.cached        = ref.attrs["cached"]
    com.pickled_data  = enc(ref.attrs["pickled_data"])
    com.pickled_data  = decode64(&com.pickled_data)
    com.event_index   = ref.attrs["event_index"]


cdef inline restore_event(ref, event_t* ev):
    restore_base(ref, ev)
    ev.commit_hash   = enc(ref.attrs["commit_hash"])
    ev.deprecated    = ref.attrs["deprecated"]
    ev.event         = ref.attrs["event"]



cdef inline restore_graph(ref, graph_t* gr):
    restore_base(ref, gr)

    gr.train            = ref.attrs["train"]
    gr.evaluation       = ref.attrs["evaluation"]
    gr.validation       = ref.attrs["validation"]

    gr.empty_graph      = ref.attrs["empty_graph"]
    gr.skip_graph       = ref.attrs["skip_graph"]
    gr.self_loops       = ref.attrs["self_loops"]

    gr.errors           = _decoder(ref.attrs["errors"])
    gr.presel           = _decoder(ref.attrs["presel"])
    gr.src_dst          = _decoder(ref.attrs["src_dst"])
    gr.hash_particle    = _decoder(ref.attrs["hash_particle"])
    gr.graph_feature    = _decoder(ref.attrs["graph_feature"])
    gr.node_feature     = _decoder(ref.attrs["node_feature"])
    gr.edge_feature     = _decoder(ref.attrs["edge_feature"])
    gr.pre_sel_feature  = _decoder(ref.attrs["pre_sel_feature"])

    gr.topo_hash        = enc(ref.attrs["topo_hash"])
    gr.graph            = ref.attrs["graph"]



cdef inline restore_selection(ref, selection_t* sel):
    restore_base(ref, sel)

    sel.errors                = _decoder(ref.attrs["errors"])
    sel.pickled_strategy_data = enc(ref.attrs["pickled_strategy_data"])
    sel.pickled_strategy_data = decode64(&sel.pickled_strategy_data)

    sel.cutflow               = _decoder(ref.attrs["cutflow"])
    sel.timestats             = ref.attrs["timestats"]
    sel.all_weights           = ref.attrs["all_weights"]
    sel.selection_weights     = ref.attrs["selection_weights"]

    sel.allow_failure         = ref.attrs["allow_failure"]
    sel._params_              = enc(ref.attrs["_params_"])
    sel._params_              = decode64(&sel._params_)
    sel.selection             = ref.attrs["selection"]



