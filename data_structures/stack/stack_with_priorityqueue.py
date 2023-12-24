from priority_queue import PriorityQueue

class StackWithPQ:
    def __init__(self):
        self.PQ = PriorityQueue()
        self.count = 0

    def push(self,val):
        self.count -= 1
        self.PQ.enqueue([self.count, val])

    def pop(self):
        if self.count == 0:
            return 'Empty'
        self.count += 1
        return self.PQ.dequeue()[1]
    
    def is_empty(self):
        return self.count == 0
    
    def show(self):
        self.PQ.heap.show()


if __name__ == '__main__':

    stack = StackWithPQ()
    stack.show()    # []
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.show()     # [[-1,1],[-2,2],[-1,3]]
    
    print(stack.pop())  # 3
    print(stack.pop())  # 2
    print(stack.pop())  # 1
    print(stack.pop())  # Empty
