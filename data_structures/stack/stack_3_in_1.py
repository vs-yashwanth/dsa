class Stack3in1:

    def __init__(self, size):
        self.size = size
        self.top1 = -1
        self.top2 = size
        self.start3 = size//2-1
        self.top3 = size//2-1
        self.array = [None] * size

    def middle_shift(dir):
        pass

    def push1(self, val):
        if self.top1 < self.start3:
            self.top1 += 1
            self.array[self.top1] = val
        else:
            shifted = self.middle_shift('right')
            if shifted:
                self.top1 += 1
                self.array[self.top1] = val
            else:
                print('Stack 1 overflow')
            
    def push2(self,val):
        if self.top2 > self.top3+1:
            self.top2 -= 1
            self.array[self.top2] = val
        else:
            shifted = self.middle_shift('left')
            if shifted:
                self.top2 -= 1
                self.array[self.top2] = val
            else:
                print('Stack 2 overflow')
            
    def push3(self,val):
        if self.top3 < self.top2-1:
            self.top3 += 1
            self.array[self.top3] = val
        else:
            shifted = self.middle_shift('left')
            if shifted:
                self.top3 += 1
                self.array[self.top3] = val
            else:
                print('Stack 3 overflow')

    def middle_shift(self,dir):
        if dir == 'right':
            if self.top3 < self.top2-1:
                temp = self.array[self.top3]
                for i in range(self.top3, self.start3,-1):
                    self.array[i] = self.array[i-1]
                self.top3 += 1
                self.array[self.top3] = temp
                self.start3 += 1
                return True
            else:
                return False
        
        if dir == 'left':
            if self.start3 > self.top1:
                temp = self.array[self.start3+1]
                for i in range(self.start3+1, self.top3+1):
                    self.array[i] = self.array[i+1]    
                self.array[self.start3] = temp
                self.start3 -= 1
                self.top3 -= 1
                return True
            else:
                return False
    
    def pop1(self):
        if self.top1 >= 0:
            out = self.array[self.top1]
            self.array[self.top1] = None
            self.top1 -= 1
            return out
        else:
            print('Stack 1 undeflow')

    def pop2(self):
        if self.top2 < self.size:
            out = self.array[self.top2]
            self.array[self.top2] = None
            self.top2 += 1
            return out
        else:
            print('Stack 2 underflow')

    def pop3(self):
        if self.top3 > self.start3:
            out = self.array[self.top3]
            self.array[self.top3] = None
            self.top3 -= 1
            return out
        else:
            print('Stack 3 underflow')
    
    def show(self):
        print(self.array)

    def show_state(self):
        print(1,self.array[self.top1])
        print(2,self.array[self.top2])
        print(3,self.array[self.top3])



if __name__ == '__main__':

    stack = Stack3in1(10)
    stack.push2(1)
    stack.push2(2)
    stack.push2(3)
    stack.push1(4)
    stack.push1(5)
    stack.push1(6)
    stack.show()
    stack.push3('a')
    stack.push3('b')
    stack.push3('c')
    stack.show()
    print(stack.pop1())
    print(stack.pop1())
    print(stack.pop1())
    stack.push1('x')
    stack.show_state()
    stack.show()

    

    
