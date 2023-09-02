def triplets(A):    # O(n**2), O(n)
    n = len(A)
    for i in A:
        target = i**2
        s = set()
        for j in range(n):
            pot = target - A[j]**2 
            if pot in s:
                return (i,A[j],int((pot)**(0.5)))
            else:
                s.add(A[j]**2)
    return -1


def triplets2(A):   # O(n**2), O(1)
    n = len(A)
    A = [i**2 for i in A]
    A.sort()

    for k in range(n):
        i = 0
        j = n-1
        while i<j:
            if A[i]+A[j] == A[k]:
                return [int(i**(0.5)) for i in (A[i],A[j],A[k])]
            elif A[i]+A[j] < A[k]:
                i += 1
            else:
                j -= 1
    return -1



print(triplets([3,1,4,6,7,8,9,10,11,12]))
print(triplets2([3,1,4,6,7,8,9,10,11,12]))