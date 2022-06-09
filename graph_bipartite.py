class Graph():
 
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in range(V)]
                      for row in range(V)]
 
        self.colors = [-1 for i in range(self.V)]
    
    def bipartite(self):
        for u in range(self.V):
            if self.colors[u] == -1:
                if not self.check(u):
                    return False
        return True
    
    def check(self, u):
        self.colors[u] = 1
        q = [u]
        while q:
            temp = q.pop(0)
            if self.graph[temp][temp]:
                return False
            for v in range(self.V):
                if self.graph[u][v] and self.colors[v] == -1:
                    self.colors[v] = 1 - self.colors[u]
                    q.append(v)
                elif self.graph[u][v] and self.colors[u] == self.colors[v]:
                    return False
        return True

g = Graph(4)
g.graph = [[0, 1, 0, 1],
           [1, 0, 1, 0],
           [0, 1, 0, 1],
           [1, 0, 1, 0]]
 
print ("Yes" if g.bipartite() else "No")