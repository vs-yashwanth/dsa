from collections import defaultdict

class Graph:
    def __init__(self):
        self.G=defaultdict(list)
    def addEdge(self,u,v):
        self.G[u].append(v)
    def DFS(self,s):
        visited = set()
        self.DFS_util(s,visited)
        for i in self.G:
            if i not in visited:
                self.dfs_util(i,visited)
            
    def DFS_util(self,s,visited):
        print(s,end=' ')
        visited.add(s)
        for i in self.G[s]:
            if i not in visited:
                self.DFS_util(i,visited)
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Breadth First Traversal"
				" (starting from vertex 2)")
g.DFS(2)

