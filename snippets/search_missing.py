def main():
    a = [1,2,4,3,6]
    print(missing(a))
    print(missing2(a))
    print(missing3(a))
    print(missing4(a))
    print(missing5(a))

def missing(a):  # O(n^2)
    n = len(a)+1
    for i in range(1,n):
        if i not in a:
            return i
    else:
        return None

def missing2(a):  # O(nlogn)
    a.sort()
    for i in range(len(a)-1):
        if a[i] + 1 != a[i+1]:
            return a[i]+1

def missing3(a):   # O(n), O(n)
    n = len(a)+1
    l = [False]*n
    for i in a:
        l[i-1] = True
    for i in range(1,n):
        if not l[i-1]:
            return i
    return i

def missing4(a):  # O(n)
    n = len(a)+1
    s = n*(n+1)//2
    for i in a:
        s -= i
    return s

def missing5(a):
    n = len(a)+1
    x1 = a[0]
    for i in a[1:]:
        x1 ^= i
    x2 = 1
    for i in range(2,n+1):
        x2 ^= i
    return x1 ^ x2

main()

