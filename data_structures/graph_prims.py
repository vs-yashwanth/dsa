from graph import Graph
import heapq
from functools import reduce

# tree that touches all nodes with minimum combined edge weights

# O(ElogV)


def prims(G):

    graph = G.G
    num_nodes = len(G.nodes)
    mst = []
    pq = []
    start = (0, -1, list(graph.keys())[0])
    heapq.heappush(pq, start)
    visited = set()

    while pq and len(mst)+1 != num_nodes:
        w, u, v = heapq.heappop(pq)
        if v in visited:
            continue
        visited.add(v)
        if u != -1:
            mst.append((u, v, w))
        for nv, nw in graph[v]:
            if nv not in visited:
                heapq.heappush(pq, (nw, v, nv))

    return reduce(lambda a, b: a+b, [c for _, _, c in mst], 0), [(a, b) for a, b, c in mst]


if __name__ == "__main__":

    graph = Graph(directed=False, weighted=True)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)
    print(prims(graph))  # 37

    graph_1 = Graph(directed=False, weighted=True)
    graph_1.add_edge(0, 1, 4)
    graph_1.add_edge(0, 2, 2)
    graph_1.add_edge(1, 2, 5)
    graph_1.add_edge(1, 3, 10)
    graph_1.add_edge(2, 3, 1)

    print(prims(graph_1))  # 7

    graph_2 = Graph(directed=False, weighted=True)
    graph_2.add_edge(0, 1, 2)
    graph_2.add_edge(0, 2, 3)
    graph_2.add_edge(1, 3, 5)
    graph_2.add_edge(2, 3, 7)

    print(prims(graph_2))  # 10

    graph_3 = Graph(directed=False, weighted=True)
    graph_3.add_edge(0, 1, 1)
    graph_3.add_edge(0, 2, 3)
    graph_3.add_edge(1, 2, 4)
    graph_3.add_edge(1, 3, 2)
    graph_3.add_edge(2, 3, 5)
    print(prims(graph_3))  # 6

    graph_4 = Graph(directed=False, weighted=True)
    graph_4.add_edge(0, 1, 2)
    graph_4.add_edge(0, 2, 5)
    graph_4.add_edge(1, 3, 4)
    graph_4.add_edge(2, 3, 1)

    print(prims(graph_4))  # 7
