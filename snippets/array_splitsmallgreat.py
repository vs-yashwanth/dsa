def split_naive(A):    # O(n**2)
    n = len(A)
    for i in range(1,n-1):

        if max(A[:i]) < A[i] < min(A[i+1:]):
            return i
    return -1

def split_optim(A):    # O(n), O(n)
    n = len(A)

    leftmax = [0]*n
    maxi = -float('inf')
    for i in range(n):
        maxi = max(maxi, A[i])
        leftmax[i] = maxi

    mini = float('inf')
    rightmin = [0]*n
    for i in range(n-1,-1,-1):
        mini = min(mini,A[i])
        rightmin[i] = mini
    
    for i in range(1,n-1):
        if A[i] > leftmax[i-1] and A[i] < rightmin[i+1]:
            return i
    return -1

def split_optim2(A):   # O(n), O(1)
    # geeksforgeeks
    pass



A = [5, 1, 4, 3, 6, 8, 10, 7, 9]
print(split_naive(A))
print(split_optim(A))