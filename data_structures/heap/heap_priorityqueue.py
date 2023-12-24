class PriorityQueue:
    
    def __init__(self):
        self.heap = []
        self.size = 0
        self.pos = {}
    
    def add(self,v,w):
        self.heap.append([v,w])
        self.pos[v] = self.size
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
        while index > 0 and self.heap[index][1] < self.heap[index//2][1]:
            self.pos[self.heap[index][0]] = index//2
            self.pos[self.heap[index//2][0]] = index
            self.heap[index], self.heap[index//2] = self.heap[index//2], self.heap[index]
        
        index = index//2
    
    def in_heap(self,v):
        return self.pos[v] < self.size
    

if __name__ == '__main__':
    pq = PriorityQueue()
    pq.add('apple',1)
    pq.add('banana',2)
    pq.add('cat',100)
    print(pq.extract_min())
    pq.decrease_key('cat',0)
    print(pq.extract_min())