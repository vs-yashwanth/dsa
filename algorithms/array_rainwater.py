# find water collected in a array heightmap

def naive(A,n):     # O(n**2), O(1)
    water = 0
    for i in range(1,n-1):
        lmax = max(A[:i])
        rmax = max(A[i+1:])
        water += max( min(lmax,rmax) - A[i] , 0)
    return water


def method1(A,n):   # O(n), O(n)

    maxi = -float('inf')
    leftmax = [0]*n
    for i in range(1,n-1):
        maxi = max(maxi, A[i])
        leftmax[i] = maxi
    
    maxi = -float('inf')
    rightmax = [0]*n
    for i in range(n-2,0,-1):
        maxi = max(maxi,A[i])
        rightmax[i] = maxi
    
    water = 0
    for i in range(1,n-1):
        left = leftmax[i]
        right = rightmax[i]
        water += max(min(left,right) - A[i], 0 )
    
    return water

def method1_optim(A,n):   # O(n), O(1)

    left_max = right_max = -float('inf')
    i = 0
    j = n-1
    water = 0
    while i<=j:
        if A[i] < A[j]:
            if A[i] > left_max:
                left_max = A[i]
            else:
                water += left_max - A[i]
            i += 1
        else:
            if A[j] > right_max:
                right_max = A[j]
            else:
                water += right_max - A[j]
            j -= 1
    return water

if __name__ == "__main__" :
 
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    n = len(arr)
     
    print(naive(arr, n))
    print(method1(arr,n))
    print(method1_optim(arr,n))