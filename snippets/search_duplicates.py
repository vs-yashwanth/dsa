def main():
    a = [0,1,2,4,3,5,1]
    print(is_dup(a))
    print(is_dup2(a))
    print(is_dup3(a))
    print(is_dup4(a))

def is_dup(a): # O(n^2)
    n = len(a)
    for i in range(n):
        if a[i] in a[i+1:]:
            return True
    return False

def is_dup2(a):  # O(nlog(n))
    a.sort()
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return True
    return False

def is_dup3(a):  # O(n), O(n)
    s=set()
    for i in a:
        if i in s:
            return True
        else:
            s.add(i)
    return False

def is_dup4(a):  # O(n) 
    """ 1) elements are from 0 to n-1
        2) elements are positive
        3) modifies the array"""

    for i in a:
        if a[i] >= 0:
            a[i] *= -1
        else:
            return True
    return False

main()