from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
from queue_py import QueueRaw


class Graph:
    def __init__(self, directed=True, weighted=False):
        self.G = defaultdict(list)
        self.directed = directed
        self.weighted = weighted
        self.nodes = set()

    def add_edge(self, u, v, w=0):
        if self.directed:
            self.add_directed_edge(u, v, w)
        else:
            self.add_undirected_edge(u, v, w)

    def add_directed_edge(self, u, v, w):
        self.G[u].append((v, w) if self.weighted else v)
        self.nodes.add(u)
        self.nodes.add(v)

    def add_undirected_edge(self, u, v, w):
        self.add_directed_edge(u, v, w)
        self.add_directed_edge(v, u, w)

    def dfs(self, start=None):
        out = []
        visited = set()
        if start:
            self.dfs_aux(start, out, visited)
        for node in list(self.G.keys()):
            if node not in visited:
                self.dfs_aux(node, out, visited)
        return out

    def dfs_aux(self, node, out, visited):
        visited.add(node)
        out.append(node)
        for neighbour in self.G[node]:
            if neighbour not in visited:
                self.dfs_aux(neighbour, out, visited)

    def bfs(self, start):
        out = []
        visited = set()
        queue = QueueRaw()
        queue.enqueue(start)
        while not queue.is_empty():
            node = queue.dequeue()
            visited.add(node)
            out.append(node)
            for neighbour in self.G[node]:
                if neighbour not in visited:
                    queue.enqueue(neighbour)
        return out

    def visualize(self):
        nx_graph = nx.DiGraph(self.G)
        nx.draw_networkx(nx_graph, **{
            'arrows': True,
            'font_color': 'white',
            'node_color': 'gray',
            'node_size': 400,
            'width': 1,
            'arrowstyle': '-|>',
            'arrowsize': 20,
        })
        plt.show()


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

    print(G.dfs(5))
    print(G.bfs(0))
    G.visualize()
