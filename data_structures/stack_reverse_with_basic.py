# reverse a given stack using only
# push and pop operations

from stack import StackRaw

def reverse_with_push_pop(stack):
    stack2 = StackRaw()
    while not stack.is_empty():
        stack2.push(stack.pop())
    return stack2


if __name__ == '__main__':
    stack = StackRaw()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.show() # 1 2 3 4
    stack = reverse_with_push_pop(stack)
    stack.show() # 4 3 2 1