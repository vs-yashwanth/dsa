class Stack:
    def __init__(self):
        self.s = []
    def push(self,data):
        self.s.append(data)
    def pop(self):
        return self.s.pop()
    def peek(self):
        return self.s[-1]
    def show(self):
        print(self.s)

class queue1:
    """ making enqueue costly """
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self,data):
        while self.s1.s:
            self.s2.push(self.s1.pop())
        self.s1.push(data)
        while self.s2.s:
            self.s1.push(self.s2.pop())
    
    def dequeue(self):
        return self.s1.pop()
    
    def show(self):
        print(self.s1.s)

class queue2:
    """ making deque costly """
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def enqueue(self,data):
        self.s1.push(data)
    
    def dequeue(self):
        if not self.s2.s:
            while self.s1.s:
                self.s2.push(self.s1.pop())
            return self.s2.pop()
        else:
            return self.s2.pop()
    def show(self):
        print(self.s1.s)

if __name__ == '__main__':
    q1 = queue1()
    q1.enqueue(0)
    q1.enqueue(1)
    q1.enqueue(2)
    q1.show()
    print(q1.dequeue())

    q2 = queue2()
    q2.enqueue(2)
    q2.enqueue(1)
    q2.enqueue(0)
    q2.show()
    print(q2.dequeue())