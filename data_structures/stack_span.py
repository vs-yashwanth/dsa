def main():
    l = [10, 4, 5, 90, 120, 80]
    print(naive(l))
    print(linear(l))

def naive(a):
    n = len(a)
    s = [1]*n
    for i in range(1,n):
        j=i-1
        while j>=0 and a[j]<=a[i]:
            s[i]+=1
            j-=1
    return s

def linear(a):
    n=len(a)
    s = [0]*n
    s[0] = 1
    stack = [0]
    for i in range(1,n):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        if stack:
            s[i] = i - stack[-1]
        else:
            s[i] = i + 1
        stack.append(i)    
    return s        


main()