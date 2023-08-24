def buysell(A):  # O(n)
    n = len(A)
    i = 0
    while i<n-1:
        if i==n-1:
            break
        while i<n-1 and A[i+1]<A[i]:
            i += 1
        buy = i

        while i<n-1 and A[i+1]>=A[i]:
            i += 1
        sell = i

        print(buy,sell)


prices =  [100, 180, 260, 310, 40, 535, 695]
buysell(prices)

