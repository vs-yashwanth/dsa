from stack import StackRaw

def prefix_to_infix(prefix):
    stack = StackRaw()
    operators = {'-','+','*','/','^'}
    prefix = prefix[::-1]
    for i in prefix:
        if i in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push(f'({op1}{i}{op2})')

        else:
            stack.push(i)
    
    return stack.pop()


if __name__ == '__main__':
    print(prefix_to_infix('*+AB+CD'))