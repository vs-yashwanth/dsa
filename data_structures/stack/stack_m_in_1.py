class StackKin1:
    def __init__(self,size,k):
        self.size = size
        self.array = [None]*size
        self.tops = [None]*k
        self.nexts = [i+1 for i in range(size)]
        self.nexts[-1] = None
        self.free = 0

    def push(self, stack_num, val):
        if self.free == None:
            print('Stack overflow')
            return
        ind = self.free
        self.array[ind] = val
        self.free = self.nexts[ind]
        self.nexts[ind] = self.tops[stack_num]
        self.tops[stack_num] = ind

    def pop(self, stack_num):
        if self.tops[stack_num] == None:
            return f'Stack {stack_num} underflow'
        ind = self.tops[stack_num]
        out = self.array[ind]
        self.tops[stack_num] = self.nexts[ind]
        self.nexts[ind] = self.free
        self.free = ind
        self.array[ind] = None
        return out
    
    def peek(self, stack_num):
        if self.tops[stack_num] == None:
            return f'Stack {stack_num} is empty'
        out = self.array[self.tops[stack_num]]
        return out
    
    def show(self):
        print(self.array)




if __name__ == '__main__':
    
    size = 15
    k = 4
    stacks = StackKin1(size,k)

    # Test 1: Push elements onto different stacks
    stacks.push(0, 5)
    stacks.push(1, 15)
    stacks.push(2, 25)
    stacks.push(3, 35)

    # Test 2: Pop elements from different stacks
    print(stacks.pop(0))  # Output: 5
    print(stacks.pop(1))  # Output: 15
    print(stacks.pop(2))  # Output: 25
    print(stacks.pop(3))  # Output: 35

    # Test 3: Push elements onto various stacks
    stacks.push(1, 10)
    stacks.push(0, 20)
    stacks.push(2, 30)
    stacks.push(1, 40)
    stacks.push(2, 50)

    # Test 4: Pop elements from different stacks
    print(stacks.pop(0))  # Output: 20
    print(stacks.pop(1))  # Output: 40
    print(stacks.pop(2))  # Output: 50

    # Test 5: Peek into stacks with elements
    print(stacks.peek(0))  # Output: None
    print(stacks.peek(1))  # Output: 10
    print(stacks.peek(2))  # Output: 30

    # Test 6: Pop elements from empty stacks
    print(stacks.pop(0))  # Output: Stack Underflow
    print(stacks.pop(1))  # Output: 10
    print(stacks.pop(2))  # Output: 30

    # Test 7: Push elements on different stacks
    stacks.push(1, 55)
    stacks.push(2, 60)
    stacks.push(3, 65)

    # Test 8: Peek into stacks with elements
    print(stacks.peek(1))  # Output: 55
    print(stacks.peek(2))  # Output: 60
    print(stacks.peek(3))  # Output: 65

    # Test 9: Push and pop on different stacks
    stacks.push(1, 70)
    print(stacks.pop(1))  # Output: 70
