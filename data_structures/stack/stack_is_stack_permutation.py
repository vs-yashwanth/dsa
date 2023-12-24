from stack import StackRaw

def is_stack_permutation(input, output):
    if len(input) != len(output): return False
    stack = StackRaw()
    for i in input:
        stack.push(i)
        while not stack.is_empty() and stack.peek() == output[0]:
            stack.pop()
            output.pop(0)
    return stack.is_empty()

if __name__ == '__main__':

    print(is_stack_permutation([4,5,6,7,8], [8,7,6,5,4]))
    print(is_stack_permutation([1,2,3,4,5,6], [3,2,5,6,4,1]))
    print(is_stack_permutation([1,2,3,4,5,6], [1,5,4,6,2,3]))