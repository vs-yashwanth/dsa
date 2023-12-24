from stack import StackRaw

def postfix_to_prefix(postfix):
    stack = StackRaw()
    operators = {'-','+','*','/','^'}
    for i in postfix:
        if i in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push(i+op2+op1)
        else:
            stack.push(i)
    
    return stack.pop()


if __name__ == '__main__':
    print(postfix_to_prefix('ABC/-AK/L-*'))