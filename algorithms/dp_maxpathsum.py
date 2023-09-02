
def naive(M,m,n):     # O(3**n)

    if m<0 or n<0:
        return float('inf')
    elif m==0 and n==0:
        return M[m][n]
    else:
        return M[m][n] + min(naive(M,m-1,n), naive(M,m,n-1), naive(M,m-1,n-1))

def memoized(M,m,n,memo={}):    # O(mn)
    if m<0 or n<0:
        return float('inf')
    elif m==0 and n==0:
        return M[m][n]
    else:
        memo[(m,n)] = M[m][n] + min(naive(M,m-1,n), naive(M,m,n-1), naive(M,m-1,n-1))
        return memo[(m,n)]
    
def bottomup(M,m,n):         # O(mn)
    table = [[0 for i in range(len(M))] for j in range(len(M[0]))]
    table[0][0] = M[0][0]
    for i in range(1,m+1):
        table[i][0] = table[i-1][0] + M[i][0]
    for j in range(1,n+1):
        table[0][j] = table[0][j-1] + M[0][j]
    for i in range(1,m+1):
        for j in range(1,n+1):
            table[i][j] = M[i][j] + min(table[i-1][j-1], table[i-1][j], table[i][j-1])
    return table[m][n]


cost= [ [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3] ]
print(naive(cost,2, 2))
print(memoized(cost,2,2))
print(bottomup(cost,2,2))