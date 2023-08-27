from linkedlist_single import SingleLinkedList
from collections import deque

# implement with arrays


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


# implement with a dequeue

class QueueWithDeque:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if not self.queue:
            return 'Empty queue'
        return self.queue.popleft()

    def peek(self):
        if not self.queue:
            return 'Empty queue'
        out = self.queue.popleft()
        self.queue.appendleft(out)
        return out

    def show(self):
        print(self.queue)

    def is_empty(self):
        return not bool(self.queue)

    def size(self):
        return len(self.queue)

    def reverse(self):
        self.queue.reverse()




# implement from scratch

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class QueueRaw:
    def __init__(self):
        self.front = None
        self.rear = None
        self.temp = None

    def enqueue(self, val):
        node = Node(val)
        if not self.front:
            self.front = node
            self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if not self.front:
            return 'Empty queue'
        out = self.front
        self.front = self.front.next
        return out.val

    def peek(self):
        if not self.front:
            return 'Empty queue'
        return self.front.val

    def show(self):
        cur = self.front
        if not cur: return 'Empty queue'
        while cur:
            print(cur.val, end=' ')
            cur = cur.next
        print()

    def size(self):
        cur = self.front
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def is_empty(self):
        return not bool(self.front)
    

    def reverse(self):
        cur = self.front
        if not cur:
            return 'Empty queue'
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.rear = self.front
        self.front = prev

    def reverse_recursive(self, node):
        if not node:
            return
        val = self.dequeue()
        self.reverse_recursive(node.next)
        self.enqueue(val)
        if node is self.rear:
            self.temp = self.front
            self.front = node
        if node is self.temp:
            self.rear = node

if __name__ == '__main__':

    queue_class = QueueRaw

    # Initialize an empty queue
    queue = queue_class()

    # Test enqueue method
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Test show method
    queue.show()

    # Test size method
    print("Size after enqueues:", queue.size())  # Expected: 3

    # Test peek method
    print("Peek:", queue.peek())  # Expected: 1

    # Test is_empty method
    print("Is empty:", queue.is_empty())  # Expected: False

    # Test dequeue method
    print("Dequeue:", queue.dequeue())  # Expected: 1
    print("Dequeue:", queue.dequeue())  # Expected: 2

    # Test size after dequeues
    print("Size after dequeues:", queue.size())  # Expected: 1

    # Test dequeue from an empty queue
    empty_queue = queue_class()
    print("Dequeue from empty queue:", empty_queue.dequeue())  # Expected: None

    # Test is_empty with an empty queue
    print("Is empty (empty queue):", empty_queue.is_empty())  # Expected: True

    # Test peek on an empty queue
    print("Peek (empty queue):", empty_queue.peek())  # Expected: None

    # Test reverse method
    empty_queue.enqueue(1)
    empty_queue.enqueue(2)
    empty_queue.enqueue(3)
    empty_queue.enqueue(4)
    empty_queue.enqueue(5)
    empty_queue.reverse()
    empty_queue.show() # 3 2 1
    empty_queue.reverse_recursive(empty_queue.front)
    empty_queue.show() # 1 2 3


