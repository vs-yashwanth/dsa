from queue_py import QueueRaw


class Stack1:
    # make push costly
    def __init__(self):
        self.q1 = QueueRaw()
        self.q2 = QueueRaw()

    def push(self, val):
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1.enqueue(val)
        while not self.q2.is_empty():
            self.q1.enqueue(self.q2.dequeue())

    def pop(self):
        return 'Stack underflow' if self.q1.is_empty() else self.q1.dequeue()

    def peek(self):
        return 'Stack underflow' if self.q1.is_empty() else self.q1.peek()

    def show(self):
        self.q1.show()


class Stack2:
    # make pop costly

    def __init__(self):
        self.q1 = QueueRaw()
        self.q2 = QueueRaw()

    def push(self, val):
        self.q1.enqueue(val)

    def pop(self):
        if self.q1.is_empty():
            return 'Stack underflow'
        for _ in range(self.q1.size()-1):
            self.q1.enqueue(self.q1.dequeue())
        return self.q1.dequeue()

    def peek(self):
        if self.q1.is_empty():
            return 'Stack underflow'
        for _ in range(self.q1.size()-1):
            self.q1.enqueue(self.q1.dequeue())
        out = self.q1.peek()
        self.q1.enqueue(self.q1.dequeue())
        return out

    def show(self):
        self.q1.show()


if __name__ == "__main__":

    stack_class = Stack2

    stack = stack_class()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.pop())  # 4
    print(stack.peek())  # 3
    print(stack.pop())  # 3
    print(stack.pop())  # 2
    print(stack.pop())  # 1
    print(stack.pop())  # Stack underflow
