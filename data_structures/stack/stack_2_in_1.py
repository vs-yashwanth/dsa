class Stack2in1:
    def __init__(self, size):
        self.size = size
        self.stack = [None]*size
        self.top1 = -1
        self.top2 = size

    def push1(self, val):
        self.top1 += 1  
        if self.stack[self.top1] is None:
            self.stack[self.top1] = val
        else:
            print('Stack full')
            self.top1 -=1 
    
    def push2(self,val):
        self.top2 -= 1
        if self.stack[self.top2] is None:
            self.stack[self.top2] = val
        else:
            print('Stack full')
            self.top2 += 1
        
    def pop1(self):
        if self.top1 == -1: return
        out = self.stack[self.top1]
        self.stack[self.top1] = None
        self.top1 -= 1
        return out
    
    def pop2(self):
        if self.top2 == self.size : return
        out = self.stack[self.top2]
        self.stack[self.top2] = None
        self.top2 += 1
        return out
    
    def show(self):
        print(self.stack)

if __name__ == '__main__':
    stack = Stack2in1(10)
    stack.push1(1)
    stack.push1(2)
    stack.push1(3)
    stack.show() # 1 2 3 None ... None

    stack.push2('a')
    stack.push2('b')
    stack.push2('c')
    stack.show() # 1 2 3 None ... c b a

    print(stack.pop1()) # 3
    print(stack.pop1()) # 2
    print(stack.pop1()) # 1
    print(stack.pop2()) # c
    stack.show() # None ... b a

