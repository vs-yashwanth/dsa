# https://cp-algorithms.com/data_structures/segment_tree.html
# https://www.topcoder.com/thrive/articles/range-operations-lazy-propagation


class SegmentTree:

    def __init__(self, n):
        self.size = n
        self.tree = [0] * 4 * n
        self.lazy = [0] * 4 * n
        self.root = 1

    def build(self, array):  # O(n)

        def construct(node, start, end):

            if start == end:
                self.tree[node] = array[start]
                return

            left = node * 2
            right = node * 2 + 1    
            mid = (start + end) // 2

            construct(left, start, mid)
            construct(right, mid + 1, end)

            self.tree[node] = self.tree[left] + self.tree[right]
        
        # use 1 indexing to avoid bugs with children indices
        construct(self.root, 0, self.size - 1)
    
    
    def query_nonlazy(self, start, end):  # O(logn)

        if start < 0 or end >= self.size:
            return 'Invalid Input'

        def match(node, n_start, n_end, start, end):
            if start > end:
                return 0

            if n_start == start and n_end == end:
                return self.tree[node]
            
            mid = (n_start + n_end) // 2

            left = match(node * 2, n_start, mid, start, min(mid, end))
            right = match(node * 2 + 1, mid + 1, n_end, max(mid + 1, start), end)

            return left + right

        return match(self.root, 0, self.size - 1, start, end ) 

    
    def query(self, start, end):  # O(logn)

        if start < 0 or end >= self.size:
            return 'Invalid Input'
        
        def match(node, n_start, n_end, start, end):

            if self.lazy[node] > 0:
                self.tree[node] += (n_end - n_start + 1) * self.lazy[node]
                if n_start != n_end:
                    self.lazy[node * 2] += self.lazy[node]
                    self.lazy[node * 2 + 1] += self.lazy[node]
                self.lazy[node] = 0

            if (n_start > n_end) or (end < n_start or start > n_end):
                return 0

            if start <= n_start and end >= n_end:
                return self.tree[node]

            mid = (n_start + n_end) // 2
            left = match(node * 2, n_start, mid, start, min(end, mid))
            right = match(node * 2 + 1, mid + 1, n_end, max(mid + 1, start), end )

            return left + right
        
        return match(self.root, 0, self.size - 1, start, end)



    def update(self, index, value):  # O(logn)

        if not 0 <= index < self.size:
            return "Invalid Input"
        
        def update_index(node, start, end, index, value):

            if start == end:
                self.tree[node] = value
                return
            
            mid = (start + end) // 2
            if index <= mid:
                update_index(node * 2, start, mid, index, value)
            else:
                update_index(node * 2 + 1, mid + 1, end, index, value)
            
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
        
        update_index(self.root, 0, self.size - 1, index, value)


    def range_update(self, start, end, value):  # O(logn) - lazy propogation

        if start < 0 or end >= self.size:
            return 'Invalid Input'
        
        def update_range(node, n_start, n_end, start, end, value):

            if self.lazy[node] > 0:
                self.tree[node] += (n_end - n_start + 1) * self.lazy[node]
                if n_start != n_end:
                    self.lazy[node * 2] += self.lazy[node]
                    self.lazy[node * 2 + 1] += self.lazy[node]
                self.lazy[node] = 0
            
            if (n_start > n_end) or (end < n_start or start > n_end):
                return 
            
            if start <= n_start and n_end <= end:
                self.tree[node] += (n_end - n_start + 1) * value
                if n_start != n_end:
                    self.lazy[node * 2] += value
                    self.lazy[node * 2 + 1] += value
                return
            
            mid = (n_start + n_end) // 2
            update_range(node * 2, n_start, mid, start, min(mid, end), value)
            update_range(node * 2 + 1, mid + 1, n_end, max(mid + 1, start), end, value)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
        
        update_range(self.root, 0, self.size - 1, start, end, value)

    
    def __str__(self):
        return str(self.tree)
    


if __name__ == '__main__':

    nums = [1,2,3,4,5]

    segment_tree = SegmentTree(len(nums))
    segment_tree.build(nums)

    print(segment_tree.query(1,3))
    print(segment_tree.query(0,4))
    print(segment_tree.query(0,3))
    print(segment_tree.query(2,3))
    print(segment_tree.query(2,2))
    print(segment_tree.query(2,1))

    segment_tree.update(4, 0)
    print('updated')

    print(segment_tree.query(1,3))
    print(segment_tree.query(0,4))
    print(segment_tree.query(0,3))

    segment_tree.update(4, 5)
    segment_tree.range_update(0, 4, 1)
    print('updated')

    print(segment_tree.query(1,3))
    print(segment_tree.query(0,4))
    print(segment_tree.query(0,3))
    print(segment_tree.query(2,3))
    print(segment_tree.query(2,2))
    print(segment_tree.query(2,1))    

