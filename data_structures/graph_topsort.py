# where some events might occur before others
# cyclic graphs cannot be topologically sorted

from collections import defaultdict
from graph import Graph


def topological_sort(g):
    graph = g.G
    visited = set()
    out = []
    for u in list(graph.keys()):
        if u not in visited:
            dfs(u, graph, visited, out)
    return out[::-1]


def dfs(u, graph, visited, out):
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            dfs(v, graph, visited, out)
    out.append(u)


if __name__ == '__main__':

    G = Graph()
    G.add_edge(0, 1)
    G.add_edge(1, 2)
    G.add_edge(1, 6)
    G.add_edge(1, 7)
    G.add_edge(6, 8)
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(2, 5)
    print(topological_sort(G))
    G.visualize()
