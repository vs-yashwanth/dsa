from collections import defaultdict


class Graph:
    def __init__(self):
        self.G = defaultdict(list)
        self.nodes = set()

    def addEdge(self, u, v):
        self.G[u].append(v)
        self.nodes.add(u)
        self.nodes.add(v)

    def cycle(self):   # O(V+E)
        visited = set()
        solved = [False] * len(self.nodes)
        for u in self.G:
            if u not in visited:
                if self.is_cycle(u, visited, solved):
                    return True
        return False

    def is_cycle(self, u, visited, solved):
        visited.add(u)
        solved[u] = True
        for v in self.G[u]:
            if v not in visited:
                if self.is_cycle(v, visited, solved):
                    return True
            if v in visited and solved[v]:
                return True
        solved[u] = False
        return False


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.cycle())
