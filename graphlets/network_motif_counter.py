import networkx as nx
import numpy as np
import itertools


def mcounter(gr):
    """Counts motifs in a directed graph

    Not work!!!

    :param gr: A ``DiGraph`` object
    :returns: A ``dict`` with the number of each motifs, with the same keys as ``mo``
    This function is actually rather simple. It will extract all 3-grams from
    the original graph, and look for isomorphisms in the motifs contained
    in a dictionary. The returned object is a ``dict`` with the number of
    times each motif was found.::
    """
    # This function will take each possible subgraphs of gr of size 3, then
    # ompare them to the mo dict using .subgraph() and is_isomorphic
    
    mcount = {}
    nodes = gr.nodes()
    motifs = {
    'S1': nx.DiGraph([(1,2),(2,3)]),
    'S2': nx.DiGraph([(1,2),(1,3),(2,3)]),
    'S3': nx.DiGraph([(1,2),(2,3),(3,1)]),
    'S4': nx.DiGraph([(1,2),(3,2)]),
    'S5': nx.DiGraph([(1,2),(1,3)])
    }

    # All combinations of three nodes in the
    # original graph. Combinations with non-unique nodes filtred, because
    # the motifs do not account for self-consumption.

    triplets = list(itertools.product(*[nodes, nodes, nodes]))
    triplets = [trip for trip in triplets if len(list(set(trip))) == 3]
    triplets = map(list, map(np.sort, triplets))
    u_triplets = []
    [u_triplets.append(trip) for trip in triplets if not u_triplets.count(trip)]

    # For each triplet, take its subgraph, and compare
    # it to all fo the possible motifs

    for trip in u_triplets:
        sub_gr = gr.subgraph(trip)
        for i in motifs.items():
            if nx.is_isomorphic(sub_gr, i[1]):
                mcount[i[0]] += 1

    return mcount