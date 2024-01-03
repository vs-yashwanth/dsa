
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
        largest = left if left < self.size and self.heap[left][0] > self.heap[ind][0] else ind

        right = self.right_child(ind)
        largest = right if right < self.size and self.heap[
            right][0] > self.heap[largest][0] else largest
        if largest != ind:
            self.heap[ind], self.heap[largest] = self.heap[largest], self.heap[ind]
            self.heapify(largest)

    def heapify_up(self, ind):
        if ind <= 0:
            return
        parent = self.parent(ind)
        if self.heap[parent][0] < self.heap[ind][0]:
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
        return ind*2 + 2

    def heapify(self, ind):
        if ind >= self.size:
            return
        left = self.left_child(ind)
        right = self.right_child(ind)
        if left < self.size and self.heap[left][0] < self.heap[ind][0]:
            smallest = left
        else:
            smallest = ind
        if right < self.size and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != ind:
            self.heap[ind], self.heap[smallest] = self.heap[smallest], self.heap[ind]
            self.heapify(smallest)

    def heapify_up(self, ind):
        if ind == 0:
            return
        parent = self.parent(ind)
        if self.heap[ind][0] < self.heap[parent][0]:
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
    heap_with_one_element.insert([42, 'data'])
    print(heap_with_one_element.get_max())  # Expected output: 42
    print(heap_with_one_element.pop_max())  # Expected output: 42

    # Edge Test 3: Insert duplicate elements
    heap_with_duplicates = BinaryMaxHeap()
    heap_with_duplicates.insert([5, 'data'])
    heap_with_duplicates.insert([5, 'data'])
    heap_with_duplicates.insert([5, 'data'])
    heap_with_duplicates.insert([5, 'data'])
    print(heap_with_duplicates.get_max())  # Expected output: 5

    # Edge Test 4: Insert elements in descending order, then heapify
    descending_heap = BinaryMaxHeap()
    descending_heap.insert([5, 'data'])
    descending_heap.insert([4, 'data'])
    descending_heap.insert([3, 'data'])
    descending_heap.insert([2, 'data'])
    descending_heap.insert([1, 'data'])
    descending_heap.heapify(0)  # Heapify the descending order heap
    print(descending_heap.get_max())  # Expected output: 5

    # Edge Test 5: Insert elements in ascending order, then heapify
    ascending_heap = BinaryMaxHeap()
    ascending_heap.insert([1, 'data'])
    ascending_heap.insert([2, 'data'])
    ascending_heap.insert([3, 'data'])
    ascending_heap.insert([4, 'data'])
    ascending_heap.insert([5, 'data'])
    ascending_heap.heapify(0)  # Heapify the ascending order heap
    print(ascending_heap.get_max())  # Expected output: 5

    # Edge Test 6: Insert random elements and test heapify
    random_heap = BinaryMaxHeap()
    random_heap.insert([9, 'data'])
    random_heap.insert([2, 'data'])
    random_heap.insert([7, 'data'])
    random_heap.insert([4, 'data'])
    random_heap.insert([6, 'data'])
    random_heap.insert([3, 'data'])
    random_heap.heapify(0)
    # Expected output: 9
    print(random_heap.get_max())

    # tests for min heap ---------------------------------
    print('\nmin heap\n')
    min_heap = BinaryMinHeap()

    # Test insert method
    min_heap.insert([3, 'data'])
    min_heap.insert([5, 'data'])
    min_heap.insert([9, 'data'])
    min_heap.insert([7, 'data'])
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
    heap_with_one_element.insert([42, 'data'])
    print(heap_with_one_element.heap)  # Expected output: [42]
    print(heap_with_one_element.pop_min())  # Expected output: 42
    print(heap_with_one_element.heap)  # Expected output: []

    # Edge Test 3: Insert duplicate elements
    heap_with_duplicates = BinaryMinHeap()
    heap_with_duplicates.insert([5, 'data'])
    heap_with_duplicates.insert([5, 'data'])
    heap_with_duplicates.insert([5, 'data'])
    heap_with_duplicates.insert([5, 'data'])
    print(heap_with_duplicates.heap)  # Expected output: [5, 5, 5, 5]

    # Edge Test 4: Insert elements in ascending order, then heapify
    ascending_heap = BinaryMinHeap()
    ascending_heap.insert([1, 'data'])
    ascending_heap.insert([2, 'data'])
    ascending_heap.insert([3, 'data'])
    ascending_heap.insert([4, 'data'])
    ascending_heap.insert([5, 'data'])
    ascending_heap.heapify(0)
    print(ascending_heap.heap)  # Expected output: [1, 2, 3, 4, 5]

    # Edge Test 5: Insert elements in descending order, then heapify
    descending_heap = BinaryMinHeap()
    descending_heap.insert([5, 'data'])
    descending_heap.insert([4, 'data'])
    descending_heap.insert([3, 'data'])
    descending_heap.insert([2, 'data'])
    descending_heap.insert([1, 'data'])
    descending_heap.heapify(0)
    print(descending_heap.heap)  # Expected output: [1, 2, 3, 5, 4]

    # Edge Test 6: Insert random elements and test heapify
    random_heap = BinaryMinHeap()
    random_heap.insert([9, 'data'])
    random_heap.insert([2, 'data'])
    random_heap.insert([7, 'data'])
    random_heap.insert([4, 'data'])
    random_heap.insert([6, 'data'])
    random_heap.insert([3, 'data'])
    random_heap.heapify(0)
    print(random_heap.heap)  # Expected output: The min heap after heapify
