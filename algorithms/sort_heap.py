import random

class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def build_heap(self, array):
        self.size = len(array)
        self.heap = array
        for i in range(self.size//2,-1,-1):
            self.heapify_down(i)

    def parent(self, i):
        return i//2
    
    def left_child(self, i):
        return 2*i + 1
    
    def right_child(self, i):
        return 2*i + 2
    
    def heapify_down(self, ind):
        if ind >= self.size:
            return
        left = self.left_child(ind)
        right = self.right_child(ind)
        largest = ind
        if left < self.size and self.heap[left] > self.heap[ind]:
            largest = left
        else: 
            largest = ind
        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != ind:
            self.heap[largest], self.heap[ind] = self.heap[ind], self.heap[largest]
            self.heapify_down(largest)

    def pop_max(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.size -= 1
        out = self.heap.pop()
        self.heapify_down(0)
        return out
    
def heap_sort(array):
    heap = MaxHeap()
    heap.build_heap(array)
    out = []
    for _ in range(len(array)):
        out.append(heap.pop_max())
    return out[::-1]


if __name__ == '__main__':
    n = 6
    a = list(random.sample(range(1, 10), n))

    print(a)
    a_s = a.copy()
    a_s = heap_sort(a_s)
    print(a_s)
    print(a_s == sorted(a))