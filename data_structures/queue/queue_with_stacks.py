from stack import StackRaw

class Queue1:
    # making enqueue costly
    def __init__(self):
        self.s1 = StackRaw()
        self.s2 = StackRaw()

    def enqueue(self, val):
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())
        self.s1.push(val)
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())

    def dequeue(self):
        if self.s1.is_empty():
            return 'Empty Queue'
        return self.s1.pop()

    def peek(self):
        if self.s1.is_empty():
            return 'Empty Queue'
        return self.s1.peek()

    def show(self):
        self.s1.show()


class Queue2:
    # making dequeue costly

    def __init__(self):
        self.s1 = StackRaw()
        self.s2 = StackRaw()

    def enqueue(self, val):
        self.s1.push(val)

    def dequeue(self):
        if self.s1.is_empty():
            return 'Empty queue'
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())
        out = self.s2.pop()
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())
        return out

    def peek(self):
        if self.s1.is_empty():
            return 'Empty queue'
        while self.s1.size() != 1:
            self.s2.push(self.s1.pop())
        out = self.s1.peek()
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())
        return out

    def show(self):
        self.s1.show()


if __name__ == '__main__':

    queue_class = Queue2

    # Initialize an empty queue
    queue = queue_class()

    # Test enqueue method
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Test show method
    queue.show()

    # Test peek method
    print("Peek:", queue.peek())  # Expected: 1

    # Test dequeue method
    print("Dequeue:", queue.dequeue())  # Expected: 1
    print("Dequeue:", queue.dequeue())  # Expected: 2

    # Test dequeue from an empty queue
    empty_queue = queue_class()
    print("Dequeue from empty queue:", empty_queue.dequeue())  # Expected: None

    # Test peek on an empty queue
    print("Peek (empty queue):", empty_queue.peek())  # Expected: None
