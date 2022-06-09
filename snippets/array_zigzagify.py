def method1(A):   # O(nlogn), O(1)
    n = len(A)
    A.sort()
    for i in range(1,n-1,2):
        A[i],A[i+1] = A[i+1],A[i]
    print(A)

def method2(A):   # O(n), O(1)
    n = len(A)
    flag = 0
    for i in range(n-1):
        if not flag and A[i]>A[i+1]:
            A[i],A[i+1] = A[i+1],A[i]
        if flag and A[i]<A[i+1]:
            A[i],A[i+1] = A[i+1],A[i]
        flag = not flag
    print(A)
        
arr = [4, 3, 7, 8, 6, 2, 1]
n = len(arr)
method1(arr.copy())
method2(arr.copy())