from stack import StackRaw

def postfix_evaluate(postfix):
    stack = StackRaw()
    operators = {'-','+','*','/','^'}

    for i in postfix:
        if i in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            res = evaluate(op1,op2,i)
            stack.push(res)
        else:
            stack.push(i)

    return stack.pop()

def evaluate(op1, op2, operator):
    op1, op2 = int(op1), int(op2)
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op2 - op1
    elif operator == '*':
        return op1 * op2
    elif operator == '/':
        return op2 // op1
    elif operator == '^':
        return op2 ** op1
    else:
        return 0
    

if __name__ == '__main__':
    
    print(postfix_evaluate('456*+')) # expected: 34
    print(postfix_evaluate('78+32+/')) # expected: 3


    
