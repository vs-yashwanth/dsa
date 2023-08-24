def naive(A,start,end):         # O(n**n)
    if start>=end:
        return 0
    if A[start] == 0:
        return float('inf')
    mini = float('inf')
    for i in range(start+1,start+1+A[start]):
        jumps = 1 + naive(A,i,end)
        mini = min(mini,jumps)
    return mini

def bottomup(A):
    n = len(A)
    table = [float('inf') for _ in range(n)]
    table[0] = 0
    for i in range(1,n):
        for j in range(i):
            if j+A[j] >= i and table[j] != float('inf'):
                table[i] = min(table[i], table[j]+1)
    return table[-1]

A = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
print(naive(A,0,len(A)-1))
print(bottomup(A))


