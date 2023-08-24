def lsis(A):            # O(n**2)
    n = len(A)
    table = A.copy()
    for i in range(1,n):
        for j in range(i):
            if A[i]>A[j] and table[i] < table[j]+A[i]:
                table[i] = table[j]+A[i]
    return max(table)

A = [1, 101, 2, 3, 100, 4, 5]
print(lsis(A))
