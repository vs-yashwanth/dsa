def largest0sum(A):       # O(n), O(n)

    D = {}
    max_len = 0
    run = 0
    for i in range(len(A)):
        run += A[i]
        if A[i] == 0 and max_len == 0:
            max_len = 1
        if run == 0:
            max_len = i+1
        if run in D:
            max_len = max(max_len, i - D[run])
        else:
            D[run] = i
    return max_len

arr = [15, -2, 2, -8, 1, 7, 10, 13]
print(largest0sum(arr))
