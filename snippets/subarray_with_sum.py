def subarraysum(a,n,target):
    """ subarray with the given sum"""
    i = 1
    start = 0
    here = a[0]
    while i<=n:
        while here > target and start < i-1:
            here -= a[start]
            start += 1
        
        if here == target:
            return a[start:i-1]
        
        if i<n:
            here += a[i]
        i += 1
    
    return -1
    

arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 24
 
print(subarraysum(arr, n, sum_))