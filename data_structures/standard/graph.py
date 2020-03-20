'''
We define a standard, undirected graph G=(V,E), where V is a 
set of nodes and E is a set of edges, where each edge e=(u,v)
is a pair of nodes in V.

This module defines transformations between various
representations of the structure defined above. 
'''

def adjacency_from_graph(V, E):
    '''
    Given a graph, return an adjacency map representation.
    '''
    L = {}

    for v in V:
        L[v] = set()

    for u, v in E:
        L[u].add(v)
        L[v].add(u)
    
    return L


def graph_from_adjacency(L):
    '''
    Given the adjacency map represention L of a graph, return
    the sets V and E.
    '''
    V = set([v for v in L])
    
    # Eliminate duplicates so that (u, v) and (v, u) 
    # are not both present
    E = set([frozenset([x, y]) for x, y in L[v] for v in L])

    E = set([tuple(pair) for pair in E])

    return (V, E)


def edgelist_from_graph(V, E):
    '''
    Given a graph, return an edgelist representation.

    Note: if there exist disconnected nodes, they will be
    implicitly removed from the graph per, the constraints
    of the representation.
    '''
    return [e for e in E] 


def graph_from_edgelist(L):
    '''
    Given the edgelist representation of a graph, return the sets
    V and E.
    '''
    V = set([v for v in e for e in L)
    E = set([e for e in L])
