from collections import defaultdict
from graph import Graph
from graph_topsort import topological_sort


def SSSP_dag(G, start):
    graph = G.G
    top_sorted = topological_sort(G, weighted=True)
    dist = [float('inf')]*len(list(graph.keys()))
    dist[start] = 0
    for u in top_sorted:
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u]+w

    return dist


if __name__ == '__main__':

    g = Graph(weighted=True)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 3, 6)
    g.add_edge(1, 2, 2)
    g.add_edge(2, 4, 4)
    g.add_edge(2, 5, 2)
    g.add_edge(2, 3, 7)
    g.add_edge(3, 4, -1)
    g.add_edge(4, 5, -2)

    s = 1
    print(SSSP_dag(g, s))
    # [inf, 0, 2, 6, 5, 3]
