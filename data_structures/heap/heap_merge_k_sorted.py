from priority_queue import PriorityQueue
# merge k sorted lists using PQ
# take the leading elements from all lists and
# put them in PQ and proceed until PQ is empty

def merge_k_sorted_lists(lists):
    n, k = len(lists), len(lists[0])
    pq = PriorityQueue()
    out = []
    pos = [0]*n
    for i, p in enumerate(pos):
        pq.enqueue([lists[i][p], i])

    while not pq.is_empty():
        val, ind = pq.dequeue()
        out.append(val)
        pos[ind] += 1
        if pos[ind] < n:
            pq.enqueue([lists[ind][pos[ind]], ind])

    return out


if __name__ == '__main__':

    lists = [
        [1, 3, 5, 7],
        [0, 2, 4, 6],
        [1.5, 2 , 3.5, 4.5]
    ]

    print(merge_k_sorted_lists(lists))
