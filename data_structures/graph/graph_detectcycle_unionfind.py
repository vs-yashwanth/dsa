from collections import defaultdict

class Graph:
    def __init__(self):
        self.G = defaultdict(list)
    
    def add_edge(self,u,v):
        self.G[u].append(v)
    
class DisjointSet:
    def __init__(self,n=10):
        self.rank = [1]*n
        self.parent = [i for i in range(n)]
    
    def find(self,key):
        if self.parent[key] != key:
            self.parent[key] = self.find(self.parent[key])
        return self.parent[key]
    
    def union(self,s1,s2):
        r1 = self.find(s1)
        r2 = self.find(s2)

        if r1 == r2:
            return
        if self.rank[r1] < self.rank[r2]:
            self.parent[r1] = r2
        elif self.rank[r2] < self.rank[r1]:
            self.parent[r2] = r1
        else:
            self.parent[r2] = r1
            self.rank[r1] += 1

def is_cycle(graph):

    S = DisjointSet()
    
    for u in graph.G:
        r1 = S.find(u)
        for v in graph.G[u]:
            r2 = S.find(v)
            if r1 == r2:
                return True
            else:
                S.union(u,v)
    return False


graph = Graph()

graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(3,2)

print(is_cycle(graph))