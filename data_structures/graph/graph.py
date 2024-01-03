from collections import defaultdict
# import networkx as nx
# import matplotlib.pyplot as plt
from helpers import QueueWithArray


class Graph:
    def __init__(self):
        self.G = defaultdict(list)

    def addEdge(self, u, v):
        self.G[u].append(v)

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
        queue = QueueWithArray()
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
        nx_graph = nx.Graph(self.G)
        nx.draw(nx_graph, with_labels=True, font_color='white')
        plt.show()


if __name__ == '__main__':

    G = Graph()
    G.addEdge(0, 1)
    G.addEdge(1, 2)
    G.addEdge(1, 6)
    G.addEdge(1, 7)
    G.addEdge(6, 8)
    G.addEdge(2, 3)
    G.addEdge(2, 4)
    G.addEdge(2, 5)

    print(G.dfs(5))
    print(G.bfs(0))
    # G.visualize()
