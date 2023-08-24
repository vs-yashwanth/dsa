
def leaders(A,n):
    i = n-1
    leader = A[i]
    print(leader,end=' ')
    for i in range(n-2,-1,-1):
        if A[i] >  leader:
            print(A[i],end=' ')
            leader = A[i]

arr=[16, 17, 4, 3, 5, 2]
leaders(arr, len(arr))