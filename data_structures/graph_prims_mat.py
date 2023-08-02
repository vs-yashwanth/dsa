class Graph:

    def __init__(self, n):
        self.n = n
        self.G = [[0 for _ in range(n)] for _ in range(n)]
    
    def show_mst(self, parent):
        for i in range(self.n):
            #print(parent[i], i, self.G[i][parent[i]])
            print(parent[i],i,self.G[parent[i]][i])
        
    def min_key(self, key, mst):

        mini = float('inf')
        for i in range(self.n):
            if key[i] <  mini and mst[i] == False:
                mini = key[i]
                mini_id = i
        return mini_id
    
    def prims(self):

        key = [float('inf')] * self.n
        key[0] = 0
        parent = [None] * self.n
        parent[0] = -1
        mst = [False] * self.n

        for _ in range(self.n):
            u = self.min_key(key, mst)
            mst[u] = True

            for v in range(self.n):
                if self.G[u][v] > 0 and mst[v] == False and key[v] > self.G[u][v]:
                    key[v] = self.G[u][v]
                    parent[v] = u
        self.show_mst(parent)

g = Graph(5)
g.G = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
g.prims()
