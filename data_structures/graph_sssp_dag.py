from collections import defaultdict
from graph import Graph
from graph_topsort import topological_sort

# O(V + E)

# why topological works : topological sorting ensures in an edge u,v , u is procesed before v. So as we update distances
# of nodes, if we first update the distance of each u before its v, the computed dist of v will be more accurate. If we
# process v before u, if the dist of u later updates to a smaller dist, we wouldn't be able to reflect that in the dist of v.

# https://stackoverflow.com/questions/68449275/why-do-we-need-to-perform-topological-ordering-first-to-find-shortest-path-in-a


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
