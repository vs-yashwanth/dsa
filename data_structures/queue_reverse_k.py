from queue_py import QueueRaw
from stack import StackRaw

def reverse_k(queue, k):
    stack = StackRaw()
    for _ in range(k):
        stack.push(queue.dequeue())
    for _ in range(k):
        queue.enqueue(stack.pop())
    for _ in range(queue.size() - k):
        queue.enqueue(queue.dequeue())


if __name__ == '__main__':

    queue = QueueRaw()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    reverse_k(queue, 4)
    queue.show()  # 4 3 2 1 5 6 7 8
