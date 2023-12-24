from stack import StackRaw

def infix_evaluate(infix):
    infix = infix.split(' ')
    precedance = {'-':1, '+':2, '*':3, '/':4, '^':5, '(': 10}
    operator_stack = StackRaw()
    operand_stack = StackRaw()
    for i in infix:
        if i in precedance:
            while not operator_stack.is_empty() and precedance[operator_stack.peek()] >= precedance[i]:
                if operator_stack.peek() == '(':
                    break
                op = operator_stack.pop()
                op1 = operand_stack.pop()
                op2 = operand_stack.pop()
                res = evaluate(op1, op2, op)
                operand_stack.push(res)

            operator_stack.push(i)
        
        elif i == ')':
            while not operator_stack.is_empty():
                if operator_stack.peek() == '(':
                    operator_stack.pop()
                    break
                else:
                    op = operator_stack.pop()
                    op1, op2 = operand_stack.pop(), operand_stack.pop()
                    res = evaluate(op1, op2, op)
                    operand_stack.push(res)
        elif i == ' ':
            pass

        else:
            operand_stack.push(i)

    while not operator_stack.is_empty():
        op = operator_stack.pop()
        op1 = operand_stack.pop()
        op2 = operand_stack.pop()
        res = evaluate(op1,op2,op)
        operand_stack.push(res)
    
    return operand_stack.pop()
        

def evaluate(op1,op2,op):
    op1, op2 = int(op1), int(op2)
    if op == '+':
        return op1+op2
    elif op == '-':
        return op2-op1
    elif op == '*':
        return op2*op1
    elif op == '/':
        return op2//op1
    elif op == '^':
        return op2**op1
    else:
        return 0
    

if __name__ == '__main__':
    
    print(infix_evaluate('10 + 2 * 6')) # expected: 22
    print(infix_evaluate('100 * 2 + 12')) # expected: 212
    print(infix_evaluate('100 * ( 2 + 12 )')) # expected: 1400
    print(infix_evaluate('100 * ( 2 + 12 ) / 14')) # expected: 100
    print(infix_evaluate('( ( 20 - 10 ) * ( 30 - 20 ) + 10 ) * 2')) # expected: 220
    print(infix_evaluate('( ( 20 - 10 ) * ( 30 - 20 ) / 10 + 10 ) * 2')) # expected: 40

