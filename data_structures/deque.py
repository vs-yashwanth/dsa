
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def pop(self):
        if not self.tail:
            return 'Empty deque'
        prev = self.tail.prev
        out = self.tail.val
        prev.next = None
        self.tail = prev
        return out

    def push_left(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def pop_left(self):
        if not self.head:
            return 'Empty deque'
        out = self.head.val
        self.head = self.head.next
        self.head.prev = None
        return out

    def __str__(self):
        out = ''
        cur = self.head
        while cur:
            out += f'{cur.val} '
            cur = cur.next
        return out


if __name__ == '__main__':

    # Initialize an empty deque
    deque = Deque()

    # Test push method
    deque.push(1)
    deque.push(2)
    deque.push(3)

    # Test push_left method
    deque.push_left(0)
    deque.push_left(-1)

    # Test pop method
    popped_item = deque.pop()
    print("Popped:", popped_item)  # Expected: 3

    # Test pop_left method
    popped_left_item = deque.pop_left()
    print("Popped left:", popped_left_item)  # Expected: -1

    # Print the deque after operations
    print("Deque after operations:", deque)  # Expected: [0, 1, 2]

    # Test pop from an empty deque
    empty_deque = Deque()
    popped_empty = empty_deque.pop()
    print("Popped from empty deque:", popped_empty)  # Expected: None

    # Test pop_left from an empty deque
    popped_left_empty = empty_deque.pop_left()
    print("Popped left from empty deque:", popped_left_empty)  # Expected: None
