from stack import StackRaw

def prefix_evaluate(prefix):
    stack = StackRaw()
    operators = {'-','+','*','/','^'}
    prefix = prefix[::-1]
    for i in prefix:
        if i in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            res = evaluate(op1,op2, i)
            stack.push(res)
        else:
            stack.push(i)
    return stack.pop()

def evaluate(op1, op2, operator):
    op1, op2 = int(op1), int(op2)
    if operator == '+':
        return op1+op2
    elif operator == '-':
        return op1-op2
    elif operator == '*':
        return op1*op2
    elif operator == '/':
        return op1//op2
    elif operator == '^':
        return op1**op2
    else:
        return 0


if __name__ == '__main__':
    print(prefix_evaluate('+9*26')) # expected: 21
    print(prefix_evaluate('-+8/632')) # expected: 8
    print(prefix_evaluate('-+7*45+20')) # expected: 25