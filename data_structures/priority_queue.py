from heap_with_data import BinaryMinHeap


class PriorityQueue:
    def __init__(self):
        self.heap = BinaryMinHeap()

    def enqueue(self, val):
        self.heap.insert(val)

    def dequeue(self):
        return self.heap.pop_min()

    def peek(self):
        return self.heap.get_min()

    def size(self):
        return self.heap.size

    def is_empty(self):
        return self.heap.size == 0

    def increase_key(self, key, new_key, val):
        self.heap.increase_val([key, val], [new_key, val])

    def decrease_key(self, key, new_key, val):
        self.heap.decrease_val([key, val], [new_key, val])

    def clear(self):
        self.heap = BinaryMinHeap()


if __name__ == '__main__':

    # Test Case 1: Enqueue and Dequeue
    pq = PriorityQueue()
    pq.enqueue([2, "Task 1"])  # Expected: Enqueue "Task 1" with priority 2
    pq.enqueue([1, "Task 2"])  # Expected: Enqueue "Task 2" with priority 1
    pq.enqueue([3, "Task 3"])  # Expected: Enqueue "Task 3" with priority 3
    print(pq.dequeue())  # Expected: [1, "Task 2"] (Dequeue "Task 2")

    # Test Case 2: Enqueue with the same priority
    pq = PriorityQueue()
    pq.enqueue([1, "Task A"])  # Expected: Enqueue "Task A" with priority 1
    pq.enqueue([1, "Task B"])  # Expected: Enqueue "Task B" with priority 1
    print(pq.dequeue())  # Expected: [1, "Task A"] (Dequeue "Task A")
    print(pq.dequeue())  # Expected: [1, "Task B"] (Dequeue "Task B")

    # Test Case 3: Enqueue and Dequeue from an empty queue
    pq = PriorityQueue()
    # Expected: None (Dequeue from an empty queue should return None)
    print(pq.dequeue())

    # Test Case 4: Enqueue with different data types
    pq = PriorityQueue()
    pq.enqueue([2, 5])        # Expected: Enqueue the integer 5 with priority 2
    # Expected: Enqueue the string "Hello" with priority 1
    pq.enqueue([1, "Hello"])
    print(pq.dequeue())  # Expected: [1, "Hello"] (Dequeue "Hello")
    print(pq.dequeue())  # Expected: [2, 5] (Dequeue 5)

    # Test Case 5: Change Priority
    pq = PriorityQueue()
    pq.enqueue([2, "Task 1"])
    pq.enqueue([1, "Task 2"])
    pq.enqueue([3, "Task 3"])
    pq.enqueue([4, "Task 4"])
    pq.enqueue([5, "Task 5"])

    # Change the priority of "Task 2" to 0
    pq.decrease_key(1, 0, "Task 2")

    # After changing the priority, "Task 2" should be at the front
    print(pq.dequeue())  # Expected: [0, "Task 2"] (Dequeue "Task 2")

    # Test Case 6: Peek
    pq = PriorityQueue()
    pq.enqueue([2, "Task 1"])
    pq.enqueue([1, "Task 2"])
    pq.enqueue([3, "Task 3"])
    print(pq.peek())  # Expected: [1, "Task 2"] (Peek at "Task 2")

    # Test Case 7: Size and Is Empty
    pq = PriorityQueue()
    print(pq.is_empty())  # Expected: True (Initially empty)
    pq.enqueue([2, "Task 1"])
    pq.enqueue([1, "Task 2"])
    pq.enqueue([3, "Task 3"])
    print(pq.is_empty())  # Expected: False (Not empty after enqueuing)
    print(pq.size())      # Expected: 3 (Size of the priority queue)
