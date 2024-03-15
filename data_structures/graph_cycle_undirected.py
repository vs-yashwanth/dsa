from collections import defaultdict


class Graph:
    def __init__(self):
        self.G = defaultdict(list)
        self.nodes = set()

    def addEdge(self, u, v):
        self.G[u].append(v)
        self.G[v].append(u)
        self.nodes.add(u)
        self.nodes.add(v)

    def cycle(self):   # O(V+E)
        visited = set()
        for u in self.nodes:
            if u not in visited:
                if self.is_cycle(u, visited, -1):
                    return True
        return False

    def is_cycle(self, u, visited, parent):
        visited.add(u)
        for v in self.G[u]:
            if v not in visited:
                if self.is_cycle(v, visited, u):
                    return True
            elif parent != v:
                return True
        return False


g = Graph()
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
print(g.cycle())


# ------useful resources ----------
# https://yuminlee2.medium.com/detect-cycle-in-a-graph-4461b6000845
