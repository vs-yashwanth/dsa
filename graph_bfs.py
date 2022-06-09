from collections import defaultdict

class Graph:
    def __init__(self):
        self.G= defaultdict(list)
    def addEdge(self,u,v):
        self.G[u].append(v)
    def BFS(self,s):
        visited = set()
        queue = [s]
        while queue:
            temp = queue.pop(0)
            print(temp,end=' ')
            visited.add(s)
            for i in self.G[temp]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)