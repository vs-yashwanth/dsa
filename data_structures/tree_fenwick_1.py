# 1 indexed Binary Indexed Tree / Fenwick tree
# https://cp-algorithms.com/data_structures/fenwick.html
# https://www.topcoder.com/thrive/articles/Binary%20Indexed%20Trees

class BIT:
    def __init__(self, n):      
        self.size = n
        self.bit = [0] * (n + 1)
    
    def add(self, i, val):      # O(logn)
        if not 1 <= i <= self.size:
            return "invalid"
        
        while i <= self.size:
            self.bit[i] += val
            i = i + (i & -i)
    
    def prefix_query(self, i):      # O(logn)
        if not 1 <= i <= self.size:
            return "invalid"
        
        total = 0
        while i > 0:
            total += self.bit[i]
            i = i - (i & -i)
        return total

    def range_query(self, i, j):        # O(logn)
        if not 1 <= i <= self.size or not 1 <= j <= self.size:
            return "invalid"

        return self.prefix_query(j) - self.prefix_query(i - 1)

    def build(self, array):     # O(nlogn)
        for i, val in enumerate(array):
            self.add(i + 1, val)
        
    def build_quick(self, array):       # O(n)
        for i, val in enumerate(array):
            i += 1
            self.bit[i] += val
            j = i + (i & -i)
            if j <= self.size:
                self.bit[j] += self.bit[i]


    def __str__(self):
        return ' '.join([str(num) for num in self.bit[1:]])




if __name__ == '__main__':

    def pretty_print(nums):
        print(' '.join([str(num) for num in nums]))

    nums = [1,2,3,4,5]
    bit = BIT(5)
    bit.build_quick(nums)

    pretty_print(nums)
    print(bit)

    for i in range(len(nums)):
        print(bit.prefix_query(i + 1), end = ' ')
    print()

    print(bit.range_query(2,4))

