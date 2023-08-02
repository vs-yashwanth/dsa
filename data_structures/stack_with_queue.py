class queue:
    def __init__(self):
        self.q = []
    def enqueue(self,data):
        self.q.append(data)
    def dequeue(self):
        return self.q.pop(0)
    def peek(self):
        return self.q[0]
    def show(self):
        print(self.q)

class stack1:
    """ Push is made costlier """
    def __init__(self):
        self.q1 = queue()
        self.q2 = queue()
    
    def push(self,data):
        if not self.q1.q:
            self.q1.enqueue(data)
        else:
            while self.q1.q:
                self.q2.enqueue(self.q1.dequeue())
            self.q1.enqueue(data)
            while self.q2.q:
                self.q1.enqueue(self.q2.dequeue())
    
    def pop(self):
        return self.q1.dequeue()
    def peek(self):
        return self.q1.peek()
    def show(self):
        print(self.q1.q)

class stack2:
    """ Pop is made costiler """
    def __init__(self):
        self.q1 = queue()
        self.q2 = queue()

    def push(self,data):
        self.q1.enqueue(data)

    def pop(self):
        while len(self.q1.q) != 1:
            self.q2.enqueue(self.q1.dequeue())
        temp = self.q1.dequeue()
        while self.q2.q:
            self.q1.enqueue(self.q2.dequeue())
        return temp
    def show(self):
        print(self.q1.q)

if __name__ == "__main__":
    
    s1 = stack1()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.show()
    print(s1.pop())

    s2 = stack2()
    s2.push(3)
    s2.push(2)
    s2.push(1)
    s2.show()
    print(s2.pop())
