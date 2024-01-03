class QueueWithArray:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):  # O(n) - expensive
        if not self.queue:
            return 'Empty queue'
        return self.queue.pop(0)

    def peek(self):
        if not self.queue:
            return 'Empty queue'
        return self.queue[0]

    def show(self):
        print(self.queue)

    def is_empty(self):
        return not bool(self.queue)

    def size(self):
        return len(self.queue)

    def reverse(self):
        self.queue.reverse()

    def reverse_recursive(self):
        if self.is_empty():
            return
        val = self.dequeue()
        self.reverse_recursive()
        self.enqueue(val)
