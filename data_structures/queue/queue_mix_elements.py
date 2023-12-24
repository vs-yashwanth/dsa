from queue_py import QueueRaw
from stack import StackRaw


def interleave_stack(queue):
    stack = StackRaw()
    n = queue.size()
    for _ in range(n//2):
        stack.push(queue.dequeue())
    for _ in range(n//2):
        queue.enqueue(stack.pop())
    for _ in range(n-n//2):
        queue.enqueue(queue.dequeue())
    for _ in range(n//2):
        stack.push(queue.dequeue())
    for _ in range(n//2):
        queue.enqueue(stack.pop())
        queue.enqueue(queue.dequeue())


def interleave_queue(queue):
    queue2 = QueueRaw()
    n = queue.size()
    for _ in range(n//2):
        queue2.enqueue(queue.dequeue())
    for _ in range(n//2):
        queue.enqueue(queue2.dequeue())
        queue.enqueue(queue.dequeue())
    


if __name__ == '__main__':

    fn = interleave_queue
    
    queue = QueueRaw()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)

    fn(queue)
    queue.show()  # 1 5 2 6 3 7 4 8
