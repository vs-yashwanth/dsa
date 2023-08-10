from linkedlist_single import SingleLinkedList


# impelement using arrays
class StackArray:
    def __init__(self):
        self.s = []

    def push(self,val):
        self.s.append(val)

    def pop(self):
        if len(self.s) == 0:
            return 'Stack Overflow'
        return self.s.pop()
    
    def peek(self):
        if len(self.s) == 0:
            return 'Stack Overflow'
        return self.s[-1]
    
    def is_empty(self):
        return len(self.s) == 0
    
    def delete(self):
        self.s = None

    def clear(self):
        self.s.clear()

    def size(self):
        return len(self.s)
    
    def reverse(self):
        self.s.reverse()

    def show(self):
        print(self.s)

#implement using a singly linked list

class StackLL:
    def __init__(self):
        self.s = SingleLinkedList()

    def push(self, val):
        self.s.pushLeft(val)

    def pop(self):
        if self.s.length() == 0: return 'Stack Overflow'
        return self.s.popLeft()
    
    def peek(self):
        out = self.s.popLeft()
        if out:
            self.s.pushLeft(out)
        return out

    def is_empty(self):
        if not self.s or self.s.length() == 0:
            return True
        else: return False
    
    def delete(self):
        self.s = None

    def size(self):
        return self.s.length()
    
    def reverse(self):
        return self.s.reverse()
    
    def clear(self):
        self.s = SingleLinkedList()
    
    def show(self):
        print(self.s)


# implement from scratch

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class StackRaw:
    def __init__(self):
        self.top = None
        

    def push(self,val):
        node = Node(val)
        if not self.top:
            self.top = node
        else:
            node.next = self.top
            self.top = node
    
    def pop(self):
        if not self.top:
            return 'Stack Overflow'
        else:
            out = self.top.val
            self.top = self.top.next
            return out
        
    def peek(self):
        if not self.top:
            return None
        else:
            return self.top.val
    
    def is_empty(self):
        return False if self.top else True

    def delete(self):
        self.top = None

    def size(self):
        cur = self.top
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count
    
    def reverse(self):
        cur = self.top
        if not cur or not cur.next: return cur
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        self.top = prev

    def clear(self):
        self.top = None

    def show(self):
        cur = self.top
        if not cur:
            print('Empty Stack')
            return
        while cur:
            print(cur.val, end=' ')
            cur = cur.next
        print()  

# implement from queues

# ...

if __name__ == '__main__':

    Stack = StackRaw
    
    stack = Stack()
    stack.push(5)
    stack.push(10)
    stack.push(15)
    print(stack.pop())  # Output: 15
    print(stack.pop())  # Output: 10

    # Test Case 2: Peeking at the top element
    stack.push(20)
    print(stack.peek())  # Output: 20

    # Test Case 3: Checking if the stack is empty
    print(stack.is_empty())  # Output: False
    stack.pop()
    stack.pop()
    print(stack.is_empty())  # Output: True

    # Test Case 4: Popping from an empty stack
    print(stack.pop())  # Output: None

    # Test Case 5: Size of the stack
    stack.push(30)
    stack.push(40)
    print(stack.size())  # Output: 2

    # Test Case 6: Peeking from an empty stack
    empty_stack = Stack()
    print(empty_stack.peek())  # Output: None

    # Test Case 7: Pushing and popping multiple elements
    stack = Stack()
    stack.push(5)
    stack.push(10)
    stack.push(15)
    stack.push(20)
    print(stack.pop())  # Output: 20
    print(stack.pop())  # Output: 15
    print(stack.pop())  # Output: 10
    print(stack.pop())  # Output: 5

    # Test Case 8: Mixing push and pop operations
    stack.push(25)
    print(stack.pop())  # Output: 25
    stack.push(30)
    print(stack.pop())  # Output: 30

    # Test Case 9: Testing with different data types
    stack.push("apple")
    stack.push(3.14)
    stack.push(True)
    print(stack.pop())  # Output: True
    print(stack.pop())  # Output: 3.14
    print(stack.pop())  # Output: apple

    # Test Case 10: Testing large number of push and pop operations
    large_stack = Stack()
    for i in range(10000):
        large_stack.push(i)
    for i in range(10000):
        large_stack.pop()
    print(large_stack.is_empty())  # Output: True

    # Test Case 11: Alternating push and pop
    stack.push("one")
    print(stack.pop())  # Output: one
    stack.push("two")
    print(stack.pop())  # Output: two

    # Test Case 12: Repeatedly pushing the same element
    stack.push("repeat")
    stack.push("repeat")
    print(stack.pop())  # Output: repeat
    print(stack.pop())  # Output: repeat

    # Test Case 13: Combining push, pop, and peek operations
    stack.push("first")
    stack.push("second")
    print(stack.peek())  # Output: second
    print(stack.pop())  # Output: second
    print(stack.peek())  # Output: first
    print(stack.pop())  # Output: first
    print(stack.peek())  # Output: None

    # Test Case 14: Mix of push, pop, and size operations
    stack.push("A")
    stack.push("B")
    stack.pop()
    print(stack.size())  # Output: 1
    stack.push("C")
    stack.pop()
    stack.pop()
    print(stack.size())  # Output: 0