def check(A,k):
    n = len(A)
    D = {}
    A = [i%k for i in A]
    for i in A:
        if i not in D:
            D[i] = 0
        D[i] += 1
    
    for i in A:
        if i*2 == k:
            if D[i]%2 == 1:
                return False
        elif i == 0:
            if D[i]%2 == 1:
                return False
        elif D[i] != D[k-i]:
            return False
    return True

arr = [10,20,30,40,50,60]
k = 10
n = len(arr)
print(check(arr,k))
            