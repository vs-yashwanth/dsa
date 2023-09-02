# get minimum element in O(1) time

from stack import StackRaw

class StackMinimum:
    def __init__(self):
        self.stack = StackRaw()
        self.minStack = StackRaw()
    
    def push(self, val):
        self.stack.push(val)
        if not self.minStack.is_empty():
            self.minStack.push(min(self.minStack.peek(), val))
        else:
            self.minStack.push(val)
    
    def pop(self):
        self.minStack.pop()
        return self.stack.pop()
    
    def get_minimum(self):
        return self.minStack.peek()
    


class StackMinimumEfficient:
    def __init__(self):
        self.stack = StackRaw()
        self.min_stack = StackRaw()
    
    def push(self, val):
        self.stack.push(val)
        if not self.min_stack.is_empty():
            if val <= self.min_stack.peek():
                self.min_stack.push(val)
        else:
            self.min_stack.push(val)
    
    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack.peek():
            self.min_stack.pop()
        return val
    
    def get_minimum(self):
        return self.min_stack.peek()



if __name__ == '__main__':

    min_stack = StackMinimumEfficient()
    # Test 1: Empty stack
    print("Minimum:", min_stack.get_minimum())  # Expected output: None

    # Test 2: Push and pop single element
    min_stack.push(5)
    print("Minimum:", min_stack.get_minimum())  # Expected output: 5
    min_stack.pop()
    print("Minimum:", min_stack.get_minimum())  # Expected output: None

    # Test 3: Push multiple elements
    min_stack.push(10)
    min_stack.push(5)
    min_stack.push(8)
    min_stack.push(3)
    print("Minimum:", min_stack.get_minimum())  # Expected output: 3
    min_stack.pop()
    print("Minimum:", min_stack.get_minimum())  # Expected output: 5