from graph import Graph
from union_find import DisjointSet
from functools import reduce
import heapq


def kruskals(G):
    graph = G.G
    num_nodes = len(G.nodes)
    pq = []
    for u in list(graph.keys()):
        for v, w in graph[u]:
            heapq.heappush(pq, (w, u, v))
    mst = []
    disjoint_set = DisjointSet(num_nodes)

    while len(mst)+1 != num_nodes:
        w, u, v = heapq.heappop(pq)
        u_root, v_root = disjoint_set.find(u), disjoint_set.find(v)
        if u_root != v_root:
            mst.append((u, v, w))
            disjoint_set.union(u, v)

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
    print(kruskals(graph))  # 37

    graph_1 = Graph(directed=False, weighted=True)
    graph_1.add_edge(0, 1, 4)
    graph_1.add_edge(0, 2, 2)
    graph_1.add_edge(1, 2, 5)
    graph_1.add_edge(1, 3, 10)
    graph_1.add_edge(2, 3, 1)

    print(kruskals(graph_1))  # 7

    graph_2 = Graph(directed=False, weighted=True)
    graph_2.add_edge(0, 1, 2)
    graph_2.add_edge(0, 2, 3)
    graph_2.add_edge(1, 3, 5)
    graph_2.add_edge(2, 3, 7)

    print(kruskals(graph_2))  # 10

    graph_3 = Graph(directed=False, weighted=True)
    graph_3.add_edge(0, 1, 1)
    graph_3.add_edge(0, 2, 3)
    graph_3.add_edge(1, 2, 4)
    graph_3.add_edge(1, 3, 2)
    graph_3.add_edge(2, 3, 5)
    print(kruskals(graph_3))  # 6

    graph_4 = Graph(directed=False, weighted=True)
    graph_4.add_edge(0, 1, 2)
    graph_4.add_edge(0, 2, 5)
    graph_4.add_edge(1, 3, 4)
    graph_4.add_edge(2, 3, 1)

    print(kruskals(graph_4))  # 7
