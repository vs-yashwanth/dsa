
from collections import defaultdict

class Graph:
    def __init__(self):
        self.G = defaultdict(list)
    def addEdge(self,u,v):
        self.G[u].append(v)
    def CC(self):
        visited = set()
        cc = []
        for i in self.G.copy():
            if i not in visited:
                temp = []
                cc.append(self.dfs(i,temp,visited))
        return cc
    def dfs(self,s,temp,visited):
        visited.add(s)
        temp.append(s)
        for i in self.G[s]:
            if i not in visited:
                temp = self.dfs(i,temp,visited)
        return temp

# Driver Code
if __name__ == "__main__":
    g = Graph()
 
    g.addEdge(1, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    print("Following are connected components")
    print(g.CC())

 