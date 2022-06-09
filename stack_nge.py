def main():
    a = [11,13,21,3]
    #naive_nge(a) broken
    print()
    nge_stack(a)
    
    
def naive_nge(a):
    d = {}
    for i in range(len(a)-1):
        m = max(a[i+1:])
        if a[i]>m:
            d[a[i]] = -1
        else:
            d[a[i]] = m
    d[a[-1]] = -1
    [print(f'{i} : {j}') for i,j in d.items()]

def nge_stack(a):
    stack = []
    stack.append(a[0])
    a = a[1:]
    for i in a:
        if stack and i>stack[-1]:
            print(stack.pop(),i)
        stack.append(i)
    stack = stack[::-1]
    while stack:
        print(stack.pop(),-1)
        
main()