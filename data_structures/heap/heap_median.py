from heap import BinaryMaxHeap, BinaryMinHeap

class MedianHeap:
    def __init__(self):
        self.min_heap = BinaryMinHeap()
        self.max_heap = BinaryMaxHeap()
        self.size = 0
    
    def insert(self, val):
        if self.max_heap.size == 0 or self.max_heap.get_max() >= val:
            self.max_heap.insert(val)
        else:
            self.min_heap.insert(val)
        self.size += 1
        self.balance()

    def balance(self):
        if self.max_heap.size > self.min_heap.size + 1:
            self.min_heap.insert(self.max_heap.pop_max())
        elif self.min_heap.size > self.max_heap.size:
            self.max_heap.insert(self.min_heap.pop_min())
    
    def remove(self, val):
        if val <= self.max_heap.get_max():
            self.max_heap.delete(val)
        else:
            self.min_heap.delete(val)
        self.size -= 1
        self.balance()
    
    def get_median(self):
        if self.max_heap.size == self.min_heap.size:
            return (self.max_heap.get_max()+ self.min_heap.get_min())/2
        else:
            return self.max_heap.get_max()
        


# Test the MedianHeap class
if __name__ == "__main__":
    median_heap = MedianHeap()
    
    # Test case 1
    median_heap.insert(1)
    median_heap.insert(2)
    print( median_heap.get_median())  # Expected output: 1.5
    
    # Test case 2
    median_heap.insert(3)
    print( median_heap.get_median())  # Expected output: 2.0
    
    # Test case 3
    median_heap.insert(4)
    print( median_heap.get_median())  # Expected output: 2.5

    # Test case 4: Inserting values in descending order
    median_heap = MedianHeap()
    median_heap.insert(5)
    median_heap.insert(4)
    median_heap.insert(3)
    median_heap.insert(2)
    median_heap.insert(1)
    print(median_heap.get_median())  # Expected output: 3.0

    # Test case 5: Inserting values in ascending order
    median_heap = MedianHeap()
    median_heap.insert(1)
    median_heap.insert(2)
    median_heap.insert(3)
    median_heap.insert(4)
    median_heap.insert(5)
    print(median_heap.get_median())  # Expected output: 3.0

    # Test case 6: Inserting a single value
    median_heap = MedianHeap()
    median_heap.insert(42)
    print(median_heap.get_median())  # Expected output: 42.0

    # Test case 7: Inserting negative values
    median_heap = MedianHeap()
    median_heap.insert(-1)
    median_heap.insert(-2)
    median_heap.insert(-3)
    print(median_heap.get_median())  # Expected output: -2.0

    # Test case 8: Inserting a mix of positive and negative values
    median_heap = MedianHeap()
    median_heap.insert(-5)
    median_heap.insert(5)
    median_heap.insert(-3)
    median_heap.insert(3)
    median_heap.insert(-1)
    median_heap.insert(1)
    print(median_heap.get_median())  # Expected output: 0.0

    

# references

# https://stephenjoel2k.medium.com/two-heaps-min-heap-max-heap-c3d32cbb671d
