from stack import StackRaw


def infix_to_postfix(infix):
    
    precedance = {'-': 1, '+':2, '%': 3, '/':4, '*': 5, '^': 6, '(': 10}
    operators = precedance.keys()
    stack = StackRaw()
    out = ''
    for i in infix:
        if i in operators:
            while not stack.is_empty() and precedance[stack.peek()] >= precedance[i]:
                if stack.peek() != '(':
                    out += stack.pop()
                else:
                    break
            stack.push(i)

        elif i == ')':
            while not stack.is_empty():
                if stack.peek() == '(':
                    stack.pop()
                    break
                else:
                    out += stack.pop()
        elif i == ' ':
            pass
        else:
            out += i

    while not stack.is_empty():
        out += stack.pop()
    return out



if __name__ == '__main__':


    print(infix_to_postfix('( A + B ) * ( C + D )'))
    print(infix_to_postfix("( A + B ) * C"))
    print(infix_to_postfix('A + B * C'))
    print(infix_to_postfix('2+3'))
    print(infix_to_postfix('2+3*4'))
    print(infix_to_postfix('(2+3)*4'))
    print(infix_to_postfix('5+4*3-2/1'))
    print(infix_to_postfix('a*(b+c)-d/e^f'))
    print(infix_to_postfix('a+b*c'))


