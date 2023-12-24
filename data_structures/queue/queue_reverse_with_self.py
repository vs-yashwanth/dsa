from queue_py import QueueRaw


def reverse_with_self_methods(queue):  # O(n^2), O(n)
    out = QueueRaw()
    n = queue.size()
    for i in range(n):
        for j in range(n-i-1):
            val = queue.dequeue()
            queue.enqueue(val)
        out.enqueue(queue.dequeue())
    return out


if __name__ == '__main__':
    queue = QueueRaw()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    queue = reverse_with_self_methods(queue)  # 5 4 3 2 1
    queue.show()
