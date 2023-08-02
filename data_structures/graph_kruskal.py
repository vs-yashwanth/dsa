class Graph:
    def __init__(self):
        self.G = []
        self.nodes = set()
        
    def addEdge(self,u,v,w):
        self.G.append((u,v,w))
        self.nodes.add(u)
        self.nodes.add(v)

    def find(self,parent,key):
        if parent[key] != key:
            parent[key] = self.find(parent,parent[key])
        return parent[key]
    
    def union(self,parent,rank,r1,r2):
        s1 = self.find(parent,r1)
        s2 = self.find(parent, r2)

        if s1 == s2:
            return
        if r1 < r2:
            parent[r1] = r2
        elif r2 < r1:
            parent[r2] = r1
        else:
            parent[r2] = r1
            rank[r1] += 1
    
    def kruskal(self):
        n = len(self.nodes)
        mst = []
        i, edges = 0, 0
        self.G = sorted(self.G, key = lambda x : x[2])
        parent = [i for i in range(n)]
        rank = [1]*n
        while edges < n-1:
            u, v, w = self.G[i]
            r1 = self.find(parent, u)
            r2 = self.find(parent, v)
            if r1 != r2:
                edges += 1
                mst.append((u,v,w))
                self.union(parent, rank, u,v)
            i += 1
        
        return mst

g = Graph()
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
 
print(g.kruskal())
