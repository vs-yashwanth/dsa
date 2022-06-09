from collections import defaultdict

class PriorityQueue:
    
    def __init__(self):
        self.heap = []
        self.size = 0
        self.pos = {}
    
    def add(self,v,w):
        self.heap.append([v,w])
        self.pos[v] = v
        self.size += 1
        self.heapify(0)

    
    def heapify(self, index):
        smallest = index
        left = 2*index + 1
        right = 2*index + 2

        if left < self.size and self.heap[left][1] < self.heap[smallest][1]:
            smallest = left
        if right < self.size and self.heap[right][1] < self.heap[smallest][1]:
            smallest = right
        if smallest != index:
            self.pos[ self.heap[smallest][0] ] = index
            self.pos[ self.heap[index][0] ] = smallest

            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify(index)

    def extract_min(self):
        if self.size == 0:
            return

        root = self.heap[0]
        last = self.heap[self.size - 1]
        self.heap[0] = last
        self.pos[last[0]]=0
        self.pos[root[0]]=self.size-1
        
        self.size -= 1
        self.heapify(0)

        return root
    
    def decrease_key(self, v, new):
        index = self.pos[v]
        self.heap[index][1] = new
        while index > 0 and self.heap[index][1] < self.heap[(index-1)//2][1]:
            self.pos[self.heap[index][0]] = (index-1)//2
            self.pos[self.heap[(index-1)//2][0]] = index
            self.heap[index], self.heap[(index-1)//2] = self.heap[(index-1)//2], self.heap[index]
        
        index = (index-1)//2

class Graph:
    def __init__(self):
        self.G = defaultdict(list)
        self.nodes = set()
    
    def addEdge(self,u,v,w):
        self.G[u].insert(0,(v,w))
        self.G[v].insert(0,(u,w))  # undirected
        self.nodes.add(u)
        self.nodes.add(v)
    
    def prims(self):
        n = len(self.nodes)
        key = [float('inf')]*n
        parent = [None]*n;
        key[0]=0;
        parent[0]=-1
        pq = PriorityQueue()
        for v in self.nodes:
            pq.add(v,key[v])
        
        while pq.size > 0:
            root = pq.extract_min()
            u = root[0]
            for v,w in self.G[u]:
                if pq.pos[v] < pq.size and w < key[v]:
                    key[v] = w
                    parent[v] = u
                    pq.decrease_key(v,w)
        self.show(parent)
        #print(pq.heap, pq.pos)
    
    def show(self,parent):
        for i in range(1, len(self.nodes)):
            print(parent[i], i)


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
graph.prims()




