

from collections import deque

def list_queue():  # O(n) pop
    queue=[]
    queue.append(0)
    queue.append(1)
    queue.append(2)
    queue.append(3)
    print(queue)
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))
    
def deque_queue():  # implemented as DLL
    queue = deque()
    queue.append(0)
    queue.append(1)
    queue.append(2)
    queue.append(3)
    print(queue)
    print(queue.popleft())
    print(queue.popleft())
    print(queue.popleft())
    print(queue.popleft())

list_queue()
deque_queue()

