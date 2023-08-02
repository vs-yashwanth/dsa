from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
        self.nodes = set()
    
    def addEdge(self,u,v):
        self.g[u].append(v)
        self.nodes.add(u)
        self.nodes.add(v)
    
    def topsort(self):
        
        visited = set()
        stack = []
        for i in self.nodes:
            if i not in visited:
                self.dfs(i,visited,stack)
                
        print(stack[::-1])
    
    def dfs(self,s,visited,stack):
        visited.add(s)
        for j in self.g[s]:
            if j not in visited:
                self.dfs(j,visited,stack)
        stack.append(s)

g = Graph()
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
 
print ("Following is a Topological Sort of the given graph")
 
# Function Call
g.topsort()