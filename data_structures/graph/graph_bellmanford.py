from collections import defaultdict

class Graph:
    def __init__(self):
        self.G = defaultdict(list)
        self.v = 0
        self.nodes = set()
    
    def addEdge(self,u,v,w):
        self.G[u].append((v,w))
        self.nodes.add(u)
        self.nodes.add(v)
        self.v = len(self.nodes)
    
    def BellmanFord(self,s):
        dist = [float('inf')]*self.v
        dist[s] = 0
        
        for _ in range(self.v-1):
            
            for u in self.G:
                for v,w in self.G[u]:
                    if dist[v] > dist[u]+w:
                        dist[v] = dist[u]+w
        
        for _ in range(self.v-1):
            
            for u in self.G:
                for v,w in self.G[u]:
                    if dist[v] > dist[u]+w:
                        dist[v] = - float('inf')
        
        print(dist)

g = Graph()
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
 
# Print the solution
g.BellmanFord(0)