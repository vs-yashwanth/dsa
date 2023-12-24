from heap import BinaryMaxHeap


def merge_heaps(h1, h2):  # O((m)log(n+m))
    for i in h2.heap:
        h1.insert(i)


def merge_heaps_2(h1, h2):  # O(n)
    array = []
    array += h1.heap
    array += h2.heap    
    h1.build_from_array(array)


if __name__ == '__main__':

    merge = merge_heaps_2

    heap = BinaryMaxHeap()
    heap.insert(9)
    heap.insert(6)
    heap.insert(7)
    heap.insert(4)
    heap.insert(2)
    heap.insert(3)

    heap1 = BinaryMaxHeap()
    heap1.insert(8)
    heap1.insert(5)
    heap1.insert(1)

    merge(heap, heap1)
    heap.show()
