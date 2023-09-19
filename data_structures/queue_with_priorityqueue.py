from priority_queue import PriorityQueue

class QueueWithPQ:
    def __init__(self):
        self.PQ = PriorityQueue()
        self.count = 0

    def enqueue(self, val):
        self.count += 1
        self.PQ.enqueue([self.count, val])

    def dequeue(self):
        if self.count == 0:
            return 'Empty'
        self.count -= 1
        return self.PQ.dequeue()[1]

    def is_empty(self):
        return self.count == 0

    def show(self):
        self.PQ.heap.show()


if __name__ == '__main__':

    queue = QueueWithPQ()

    queue.show()    # []
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.show()    # [[1, 1], [2, 2], [3, 3]]
    print(queue.dequeue())  # 1
    print(queue.dequeue())  # 2
    print(queue.dequeue())  # 3
    queue.show()    # []
