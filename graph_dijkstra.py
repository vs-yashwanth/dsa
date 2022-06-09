from collections import defaultdict
import heapq as pq

class Graph:
    def __init__(self):
        self.G = defaultdict(list)
        self.nodes = set()
        self.v = len(self.nodes)
    
    def addEdge(self,u,v,w):
        self.G[u].append((v,w))
        self.nodes.add(u)
        self.nodes.add(v)
        self.v = len(self.nodes)
    
    def dijkstra(self,s):
        h = []
        dist = [float('inf')]*self.v
        path = [None]*self.v
        visited = set()
        
        dist[s] = 0
        pq.heappush(h,(0,s))
        while h:
            g,u = pq.heappop(h)
            visited.add(u)
            
            for v,w in self.G[u]:
                if v not in visited:
                    f = g+w
                    if f<dist[v]:
                        dist[v] = f
                        path[v] = u
                        pq.heappush(h,(f,v))
        print(dist)
        return dist, path
    
    def shortest_path(self,s,e):
        dist, path = self.dijkstra(s)
        if dist[e]:
            return ' '.join((list(map(str,path[1:]))))
        return float('inf')

graph = Graph()
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
print(graph.shortest_path(0,5))
            
        