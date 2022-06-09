def prime(n):    # O(n^2)
    for i in range(n):
        p = True
        if i <= 1:
            continue
        for j in range(2,i-1):
            if i%j==0:
                p = False
        if p:
            print(i,end=' ')
    print()


import math
# sieve of eratosthenes
def prime2(n):   # O(nlog(logn))
    primes=[True for _ in range(n+1)]
    i=2
    while i**2 <= n:
        if primes[i] == True:
            for j in range(i**2,n+1,i):
                primes[j] = False
        i += 1
    for i in range(2,n+1):
        if primes[i]:
            print(i,end=' ')



prime(50)
prime2(50)