"""
    In a candy store, there are N different types of candies available and the prices of all the 
    N different types of candies are provided. There is also an attractive offer by the candy store. 
    We can buy a single candy from the store and 
    get at most K other candies (all are different types) for free.

Find the minimum amount of money we have to spend to buy all the N different candies.
Find the maximum amount of money we have to spend to buy all the N different candies.
"""

def min_max(A,k):       # O(nlogn)

    A.sort()
    n = len(A)
    mini = c =0
    for i in range(n):
        mini += A[i]
        c += 1+k
        if c>=n:
            break
    maxi = c = 0
    for i in range(n-1,-1,-1):
        maxi += A[i]
        c += 1+k
        if c>=n:
            break
    
    return mini,maxi

arr = [3, 2, 1, 4]
n = len(arr)
k = 2
print(min_max(arr,k))