from stack import StackRaw

def reverse_exp(exp):
    stack = StackRaw()
    for i in exp:
        stack.push(i)
    out = ''
    while not stack.is_empty():
        i = stack.pop()
        if i == '(': i = ')'
        elif i == ')': i = '('
        out += i
    return out

def infix_to_prefix(infix):
    precedance = {'-': 1, '+':2, '%': 3, '/':4, '*': 5, '^': 6, '(': 10}
    operators = precedance.keys()

    infix = reverse_exp(infix)

    stack = StackRaw()
    postfix = ''
    
    for i in infix:
        if i in operators:
            while not stack.is_empty() and precedance[stack.peek()] > precedance[i]:
                if stack.peek() != '(':
                    postfix += stack.pop()
                else:
                    break
            stack.push(i)
        elif i == ')':
            while not stack.is_empty():
                out = stack.pop()
                if out == '(':
                    break
                else:
                    postfix += out
        elif i == ' ':
            pass

        else:
            postfix += i
    
    while not stack.is_empty():
        postfix += stack.pop()
    
    prefix = reverse_exp(postfix)
    
    return prefix




if __name__ == '__main__':

    print(infix_to_prefix('(A + B) * C'))
    # * + A B C
    print(infix_to_prefix('A + B * C + D'))
    # + + A * B C D
    print(infix_to_prefix('(A + B) * (C + D)'))
    # * + A B + C D
    print(infix_to_prefix('A * B + C * D'))
    # + * A B * C D
    print(infix_to_prefix('A + B + C + D'))
    # + + + A B C D


"""
weird algo - 
1. reverse the infix exp, convert (,) to opposite
2. convert to almost postfix : pop operators with higher precedance only
3. reverse again

"""