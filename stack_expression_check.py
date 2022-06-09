def main():
    exp = "{()}[]"
    opp = {'(':')',')':'(','{':'}','}':'{','[':']',']':'['}
    print(is_balanced(exp,opp))
def is_balanced(exp,opp):
    stack = []
    for i in exp:

        if not stack:
            stack.append(i)
        elif i == opp[stack[-1]]:
            stack.pop()
        else:
            stack.append(i)
        #print(stack)
    return False if stack else True
main()