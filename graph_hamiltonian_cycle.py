class Graph():
    def __init__(self, vertices):
        self.G = [[0 for column in range(vertices)]
                            for row in range(vertices)]
        self.V = vertices
    
    def safe(self, u, pos, path):
        test = self.G[path[pos-1]][u]
        if   test == 0:
            return False
        if u in path:
            return False
        return True
    
    def hamiltonian(self):
        
        path = [-1]*self.V
        path[0] = 0
        if self.hamil( 1, path) == False:
            return False
        print(path)
        return True

    def hamil(self, pos, path):
        if pos == self.V:
            return True if self.G[path[pos-1]][path[0]]==1 else False
        
        for v in range(1, self.V):
            if self.safe(v, pos, path) == True:
                path[pos] = v
                if self.hamil(pos+1, path) == True:
                    return True
                path[pos] = -1
        return False

g1 = Graph(5)
g1.G = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0], ]
 
# Print the solution
res=g1.hamiltonian();
print(res)
g2 = Graph(5)
g2.G = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1,], [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0], ]
 
# Print the solution
res=g2.hamiltonian();
print(res)