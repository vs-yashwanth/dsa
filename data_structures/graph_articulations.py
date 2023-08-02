from collections import defaultdict

class Graph:
    def __init__(self):
        self.G = defaultdict(list)
        self.nodes = set()
        self.id = 0
        self.edges=0
    
    def addEdge(self,u,v):
        self.G[u].append(v)
        self.nodes.add(u)
        self.nodes.add(v)

    def articulations(self):
        n = len(self.nodes)

        low = [0]*n
        ids = [0]*n
        visited = set()
        art = [False]*n

        for u in self.nodes:
            if u not in visited:
                self.edges = 0
                self.dfs(u,u,-1,low,ids,art,visited)
                art[u] = self.edges>1 and art[u]
        print(art)

    def dfs(self,root,u,parent,low,ids,art,visited):
        if parent == root:
            self.edges += 1
        visited.add(u)
        self.id += 1
        low[u]=ids[u]=self.id

        for v in self.G[u]:
            if v == parent:
                continue
            if v not in visited:
                self.dfs(root,v,u,low,ids,art,visited)
                if ids[u]<low[v]:
                    art[u] = True
                if ids[u] == low[v]:
                    art[u] = True
            else:
                low[u] = min(low[u], ids[v])


g1 = Graph ()

g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
  

g1.articulations()


g3 = Graph ()
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)

g3.articulations()


g2 = Graph()
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
g2.articulations()
 