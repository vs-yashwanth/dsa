from collections import defaultdict

class Graph:
    def __init__(self):
        self.G = defaultdict(list)
        self.nodes = set()
        self.id = 0

    def addEdge(self,u,v):
        self.G[u].append(v)
        self.nodes.add(u)
        self.nodes.add(v)

    def bridges(self):
        n = len(self.nodes)
        ids = [0]*n
        low = [0]*n
        visited = set()

        bridges = []
        for u in self.nodes:
            if u not in visited:
                self.dfs(u,-1,bridges,ids,low,visited)
        return bridges

    def dfs(self,u,parent,bridges,ids,low,visited):
        visited.add(u)
        
        ids[u] = low[u] = self.id
        self.id += 1

        for v in self.G[u]:
            if v == parent:
                continue
            if v not in visited:
                self.dfs(v,u,bridges,ids,low,visited)
                low[u] = min( low[u], low[v])
                if ids[u] < low[v]:
                    bridges.append((u,v))
            else:
                low[u] = min(low[u],ids[v])

g1 = Graph()
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print(g1.bridges()) # (3,4) , (0,3)


g2 = Graph()
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print(g2.bridges()) # [(2, 3), (1, 2), (0, 1)]

g3 = Graph ()
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print(g3.bridges()) 

