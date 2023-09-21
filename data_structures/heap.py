
class BinaryMaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, ind):
        return ind//2

    def left_child(self, ind):
        return ind * 2 + 1

    def right_child(self, ind):
        return ind * 2 + 2

    def heapify(self, ind):
        if ind >= self.size:
            return
        left = self.left_child(ind)
        largest = left if left < self.size and self.heap[left] > self.heap[ind] else ind

        right = self.right_child(ind)
        largest = right if right < self.size and self.heap[right] > self.heap[largest] else largest
        if largest != ind:
            self.heap[ind], self.heap[largest] = self.heap[largest], self.heap[ind]
            self.heapify(largest)

    def heapify_up(self, ind):
        if ind <= 0:
            return
        parent = self.parent(ind)
        if self.heap[parent] < self.heap[ind]:
            self.heap[parent], self.heap[ind] = self.heap[ind], self.heap[parent]
            self.heapify_up(parent)

    def insert(self, val):
        self.heap.append(val)
        self.size += 1

        self.heapify_up(self.size-1)

    def delete(self, val):
        if self.size == 0:
            return 'Empty'
        if val not in self.heap:
            return 'Not found'
        ind = self.heap.index(val)
        self.heap[ind], self.heap[-1] = self.heap[-1], self.heap[ind]
        self.heap.pop()
        self.size -= 1
        self.heapify(ind)

    def get_max(self):
        if self.size == 0:
            return 'Empty'
        return self.heap[0]

    def pop_max(self):
        if self.size == 0:
            return 'Empty'
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        out = self.heap.pop()
        self.size -= 1
        self.heapify(0)
        return out

    def get_min(self):
        # max heap so min will be in leaf nodes
        n = self.size
        out = float('inf')
        for i in range(n//2, n):
            out = min(out, self.heap[i])
        return out

    def increase_val(self, val, new_val):
        if self.size == 0:
            return 'Empty'
        ind = self.heap.index(val)
        self.heap[ind] = new_val
        self.heapify_up(ind)

    def decrease_val(self, val, new_val):
        if self.size == 0:
            return 'Empty'
        ind = self.heap.index(val)
        self.heap[ind] = new_val
        self.heapify(ind)

    def build_from_array(self, array):  # O(n)
        # https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
        self.heap = array
        self.size = len(array)
        for i in range(self.size//2):
            self.heapify(i)

    def kth_largest(self, k):  # O(klogn )
        removed = []
        out = None
        if k > self.size:
            return out
        for i in range(k-1):
            removed.append(self.pop_max())
        out = self.pop_max()
        removed.append(out)
        for i in removed:
            self.insert(i)
        return out
    
    def kth_largest_2(self,k):  # O(n)
        prev_size = self.size
        removed = []
        self.size = min(self.size, 2**k-1)
        for _ in range(k-1):
            removed.append(self.pop_max())
        out = self.get_max()
        for i in removed:
            self.insert(i)
        self.size = prev_size
        return out

    def show(self):
        print(self.heap)


class BinaryMinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, ind):
        return ind//2

    def left_child(self, ind):
        return 2*ind + 1

    def right_child(self, ind):
        return 2*ind + 2

    def heapify(self, ind):
        if ind >= self.size:
            return
        left = self.left_child(ind)
        right = self.right_child(ind)
        if left < self.size and self.heap[left] < self.heap[ind]:
            smallest = left
        else:
            smallest = ind
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != ind:
            self.heap[ind], self.heap[smallest] = self.heap[smallest], self.heap[ind]
            self.heapify(smallest)

    def heapify_up(self, ind):
        if ind == 0:
            return
        parent = self.parent(ind)
        if self.heap[ind] < self.heap[parent]:
            self.heap[ind], self.heap[parent] = self.heap[parent], self.heap[ind]
            self.heapify_up(parent)

    def insert(self, val):
        self.heap.append(val)
        self.size += 1
        self.heapify_up(self.size-1)

    def delete(self, val):
        if self.size == 0:
            return 'Empty'
        if val not in self.heap:
            return 'Not found'
        ind = self.heap.index(val)

        self.heap[ind], self.heap[-1] = self.heap[-1], self.heap[ind]
        self.heap.pop()
        self.size -= 1
        self.heapify(ind)

    def get_min(self):
        if self.size == 0:
            return 'Empty'
        return self.heap[0]

    def pop_min(self):
        if self.size == 0:
            return 'Empty'
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        out = self.heap.pop()
        self.size -= 1
        self.heapify(0)
        return out

    def get_max(self):
        # min heap so max will be in leaf nodes
        n = self.size
        out = -float('inf')
        for i in range(n//2, n):
            out = max(out, self.heap[i])
        return out

    def increase_val(self, val, new_val):
        if self.size == 0:
            return 'Empty'
        ind = self.heap.index(val)
        self.heap[ind] = new_val
        self.heapify(ind)

    def decrease_val(self, val, new_val):
        if self.size == 0:
            return 'Empty'
        ind = self.heap.index(val)
        self.heap[ind] = new_val
        self.heapify_up(ind)

    def build_from_array(self, array):
        for i in array:
            self.insert(i)

    def kth_smallest(self, k):  # O(klogn)
        removed = []
        out = None
        if k > self.size:
            return out
        for i in range(k-1):
            removed.append(self.pop_min())
        out = self.pop_min()
        removed.append(out)
        for i in removed:
            self.insert(i)
        return out

    def kth_smallest_2(self, k):  # O(n)
        prev_size = self.size
        removed = []
        self.size = min(self.size, 2**k-1)
        for _ in range(k-1):
            removed.append(self.pop_min())
        out = self.get_min()
        for i in removed:
            self.insert(i)
        self.size = prev_size
        return out

    def show(self):
        print(self.heap)


# Test cases for MaxHeap
if __name__ == "__main__":
    # Create a max heap
    print('max heap\n')
    max_heap = BinaryMaxHeap()

    # Edge Test 1: Insert and delete in an empty heap
    empty_heap = BinaryMaxHeap()
    print(empty_heap.get_max())  # Expected output: None
    print(empty_heap.pop_max())  # Expected output: None

    # Edge Test 2: Insert and delete the only element
    heap_with_one_element = BinaryMaxHeap()
    heap_with_one_element.insert(42)
    print(heap_with_one_element.get_max())  # Expected output: 42
    print(heap_with_one_element.pop_max())  # Expected output: 42

    # Edge Test 3: Insert duplicate elements
    heap_with_duplicates = BinaryMaxHeap()
    heap_with_duplicates.insert(5)
    heap_with_duplicates.insert(5)
    heap_with_duplicates.insert(5)
    heap_with_duplicates.insert(5)
    print(heap_with_duplicates.get_max())  # Expected output: 5

    # Edge Test 4: Insert elements in descending order, then heapify
    descending_heap = BinaryMaxHeap()
    descending_heap.insert(5)
    descending_heap.insert(4)
    descending_heap.insert(3)
    descending_heap.insert(2)
    descending_heap.insert(1)
    descending_heap.heapify(0)  # Heapify the descending order heap
    print(descending_heap.get_max())  # Expected output: 5

    # Edge Test 5: Insert elements in ascending order, then heapify
    ascending_heap = BinaryMaxHeap()
    ascending_heap.insert(1)
    ascending_heap.insert(2)
    ascending_heap.insert(3)
    ascending_heap.insert(4)
    ascending_heap.insert(5)
    ascending_heap.heapify(0)  # Heapify the ascending order heap
    print(ascending_heap.get_max())  # Expected output: 5

    # Edge Test 6: Insert random elements and test heapify
    random_heap = BinaryMaxHeap()
    random_heap.insert(9)
    random_heap.insert(2)
    random_heap.insert(7)
    random_heap.insert(4)
    random_heap.insert(6)
    random_heap.insert(3)
    random_heap.heapify(0)
    # Expected output: 9
    print(random_heap.get_max())  # expected: 9
    print(random_heap.get_min())  # expected: 2

    print(random_heap.kth_largest(3))  # expected: 6
    print(random_heap.kth_largest(4))  # expected: 4

    print(random_heap.kth_largest_2(3))  # expected: 6
    print(random_heap.kth_largest_2(4))  # expected: 4

    # tests for min heap ---------------------------------
    print('\nmin heap\n')
    min_heap = BinaryMinHeap()

    # Test insert method
    min_heap.insert(5)
    min_heap.insert(9)
    min_heap.insert(3)
    min_heap.insert(7)
    print(min_heap.heap)

    # Test get_min method
    print(min_heap.get_min())  # expected: 3

    # Test delete method
    print(min_heap.delete(2))  # expected: None
    print(min_heap.heap)

    # Test pop_min method
    print(min_heap.pop_min())  # expected: 3
    print(min_heap.heap)

    # Test heapify method
    min_heap.heapify(0)
    print(min_heap.heap)

    empty_heap = BinaryMinHeap()
    print(empty_heap.heap)  # Expected output: []

    # Edge Test 2: Insert and delete the only element
    heap_with_one_element = BinaryMinHeap()
    heap_with_one_element.insert(42)
    print(heap_with_one_element.heap)  # Expected output: [42]
    print(heap_with_one_element.pop_min())  # Expected output: 42
    print(heap_with_one_element.heap)  # Expected output: []

    # Edge Test 3: Insert duplicate elements
    heap_with_duplicates = BinaryMinHeap()
    heap_with_duplicates.insert(5)
    heap_with_duplicates.insert(5)
    heap_with_duplicates.insert(5)
    heap_with_duplicates.insert(5)
    print(heap_with_duplicates.heap)  # Expected output: [5, 5, 5, 5]

    # Edge Test 4: Insert elements in ascending order, then heapify
    ascending_heap = BinaryMinHeap()
    ascending_heap.insert(1)
    ascending_heap.insert(2)
    ascending_heap.insert(3)
    ascending_heap.insert(4)
    ascending_heap.insert(5)
    ascending_heap.heapify(0)
    print(ascending_heap.heap)  # Expected output: [1, 2, 3, 4, 5]

    # Edge Test 5: Insert elements in descending order, then heapify
    descending_heap = BinaryMinHeap()
    descending_heap.insert(5)
    descending_heap.insert(4)
    descending_heap.insert(3)
    descending_heap.insert(2)
    descending_heap.insert(1)
    descending_heap.heapify(0)
    print(descending_heap.heap)  # Expected output: [1, 2, 3, 5, 4]

    # Edge Test 6: Insert random elements and test heapify
    random_heap = BinaryMinHeap()
    random_heap.insert(9)
    random_heap.insert(2)
    random_heap.insert(7)
    random_heap.insert(4)
    random_heap.insert(6)
    random_heap.insert(3)
    random_heap.heapify(0)
    print(random_heap.heap)  # Expected output: The min heap after heapify
    print(random_heap.get_max())  # expected: 9

    print(random_heap.kth_smallest(3))  # expected: 4
    print(random_heap.kth_smallest(4))  # expected: 6

    print(random_heap.kth_smallest_2(3))  # expected: 4
    print(random_heap.kth_smallest_2(4))  # expected: 6
