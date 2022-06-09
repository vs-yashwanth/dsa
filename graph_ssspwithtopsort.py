from collections import defaultdict

class Graph:
    def __init__(self):
        self.G = defaultdict(list)
        self.nodes = set()
    
    def addEdge(self,u,v,w):
        self.G[u].append((v,w))
        self.nodes.add(u)
        self.nodes.add(v)
        
    def topsort(self):
        visited = set()
        stack = []
        
        for i in self.nodes:
            if i not in visited:
                self.dfs(i,visited,stack)
        return stack[::-1]
    
    def dfs(self,s,visited,stack):
        visited.add(s)
        for i,w in self.G[s]:
            if i not in visited:
                self.dfs(i,visited, stack)
        stack.append(s)
    
    def SSSP(self,s):
        
        top = self.topsort()
        print(top)
        distances = [float('inf')]*len(self.nodes)
        
        distances[s] = 0
        for i in top:
            for node,weight in self.G[i]:
                if distances[node] > distances[i] + weight:
                    distances[node] = distances[i] + weight
        return distances

g = Graph()
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)
  
# source = 1
s = 1
  
print ("Following are shortest distances from source %d " % s)
print(g.SSSP(s))
                    
            
