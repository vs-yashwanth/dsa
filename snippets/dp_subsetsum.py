def naive(A,target,n):      # O(n!)
    if target == 0:
        return True
    if n==0:
        return False
    if A[n-1] > target:
        return naive(A,target,n-1)
    return naive(A,target,n-1) or naive(A,target-A[n-1],n-1)

def bottomup(A,target):     # O(n*t)
    n = len(A)
    table = [[False for _ in range(target+1)] for _ in range(n+1)]
    for i in range(n+1):
        table[i][0] = True
    for i in range(n+1):
        for t in range(target+1):
            if A[i-1] > t:
                table[i][t] = table[i-1][t]
            else:
                table[i][t] = table[i-1][t] or table[i-1][t-A[i-1]]
    return table[n][target]
    

A = [3, 34, 4, 12, 5, 2]
target = 9
print(naive(A,target,len(A)))
print(bottomup(A,target))
    