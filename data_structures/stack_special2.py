# stack supporting min/max with O(1) extra space

class Stack:
    def __init__(self):
        self.s = []
        self.min = 0

    def push(self,data):
        if not self.s:
            self.s.append(data)
            self.min = data
        else:
            if data>=self.min:
                self.s.append(data)
            else:
                self.s.append(2*data - self.min)
                self.min = data
    
    def pop(self):
        out = self.s.pop()
        if out >= self.min:
            return out
        else:
            old_min = self.min
            self.min = 2*self.min - out
            return old_min
    
    def min(self):
        return self.min
    
    def peek(self):
        return self.s[-1], self.min
    
    def show(self):
        print(self.s, self.min)


S = Stack()
S.push(3)
S.push(5)
S.show()
S.push(2)
S.push(1)
S.show()
print(S.pop())
S.show()
