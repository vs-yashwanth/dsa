class twostack:
    def __init__(self,n):
        self.n = n
        self.S = [None]*n
        self.t1 = -1
        self.t2 = 0
    def push1(self,data):
        if self.t1 < self.n+ self.t2:
            self.t1 += 1
            self.S[self.t1] = data
        else:
            print('Overflow')
    def push2(self,data):
        if self.t1 < self.n+self.t2:
            self.t2 -= 1
            self.S[self.t2] = data
        else:
            print('overflow')
    def pop1(self):
        if self.t1>=0:
            return self.S.pop(self.t1)
        else:
            return 'Overflow'
    def pop2(self):
        if self.t2<=-1:
            return self.S.pop(self.t2)
        else:
            return 'Overflow'
    def show(self):
        print(self.S)

def main():
    ts = twostack(5)
    ts.push1(5)
    ts.push2(10)
    ts.push2(15)
    ts.push1(11)
    ts.push2(7)
     
    print("Popped element from stack1 is " + str(ts.pop1()))
    ts.push2(40)
    print("Popped element from stack2 is " + str(ts.pop2()))
main()