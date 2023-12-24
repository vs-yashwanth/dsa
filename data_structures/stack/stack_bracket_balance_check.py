from stack import StackRaw

def check_balance(exp):
    stack = StackRaw()
    for i in exp:
        if i in '{[(':
            stack.push(i)
        else:
            if stack.is_empty(): return False
            top = stack.pop()
            if (i == ']' and top != '[') or (i=='}' and top != '{') or (i==')' and top != '('):
                return False
                
    return True if stack.is_empty() else False

if __name__ == '__main__':

    expr = "{()}[]"
    print(check_balance(expr))
    expr = "{{{}}]"
    print(check_balance(expr))
    