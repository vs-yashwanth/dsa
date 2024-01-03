from collections import defaultdict

class Graph:
    def __init__(self):
        self.G =defaultdict(list)
        self.nodes = set()
        self.sccs = 0
        self.id = 0
    
    def addEdge(self,u,v):
        self.G[u].append(v)
        self.nodes.add(u)
        self.nodes.add(v)
    
    def tarzan(self):
        n = len(self.nodes)
        ids = [-1]*n
        low = [0]*n
        stack = []
        on_stack = [False]*n
        scc = []

        for u in self.nodes:
            if ids[u] == -1:
                self.dfs(u,ids,low,stack,on_stack,scc)
        return scc
    
    def dfs(self,u,ids,low,stack,on_stack,scc):
        stack.append(u)
        on_stack[u]=True
        self.id += 1
        ids[u] = low[u] = self.id

        for v in self.G[u]:
            if ids[v] == -1:
                self.dfs(v,ids,low,stack,on_stack,scc)
            if on_stack[v]:
                low[u] = min(low[u], low[v])
        if ids[u] == low[u]:
            s = []
            node = None
            while u != node:
                node = stack.pop()
                on_stack[node]=False
                s.append(node)
                low[node] = ids[u]
                
            scc.append(s)
            self.sccs += 1

g1 = Graph()
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)

print(g1.tarzan())
  
g2 = Graph()
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print(g2.tarzan())
  
   
g3 = Graph()
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print(g3.tarzan())
  
g4 = Graph()
g4.addEdge(0, 1)
g4.addEdge(0, 3)
g4.addEdge(1, 2)
g4.addEdge(1, 4)
g4.addEdge(2, 0)
g4.addEdge(2, 6)
g4.addEdge(3, 2)
g4.addEdge(4, 5)
g4.addEdge(4, 6)
g4.addEdge(5, 6)
g4.addEdge(5, 7)
g4.addEdge(5, 8)
g4.addEdge(5, 9)
g4.addEdge(6, 4)
g4.addEdge(7, 9)
g4.addEdge(8, 9)
g4.addEdge(9, 8)
print(g4.tarzan())
  
  
g5 = Graph ()
g5.addEdge(0, 1)
g5.addEdge(1, 2)
g5.addEdge(2, 3)
g5.addEdge(2, 4)
g5.addEdge(3, 0)
g5.addEdge(4, 2)
print(g5.tarzan())




