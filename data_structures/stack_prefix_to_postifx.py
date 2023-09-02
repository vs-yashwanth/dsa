from stack import StackRaw

def prefix_to_postfix(prefix):
    stack = StackRaw()
    operators = {'+','-','*','/','^','('}
    prefix = prefix[::-1]
    for i in prefix:
        if i in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push(op1+op2+i)
        else:
            stack.push(i)

    return stack.pop()

if __name__ == '__main__':
     
    print(prefix_to_postfix('*-A/BC-/AKL'))