def count_distinct(A,k):

    D = {}
    n = len(A)
    distinct = 0
    for i in range(k):
        if A[i] not in D:
            D[A[i]] = 0
            distinct += 1
        D[A[i]] += 1
    print(distinct)
    
    for i in range(k,n):
        if D[A[i-k]] == 1:
            distinct -= 1
        D[A[i-k]] -= 1

        if A[i] not in D or D[A[i]] == 0:
            D[A[i]] = 0
            distinct += 1
        D[A[i]] += 1
        print(distinct)


arr = [1, 2, 1, 3, 4, 2, 3]
n = len(arr)
k = 4
count_distinct(arr, k)

    
