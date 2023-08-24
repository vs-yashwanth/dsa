def factors(n):   # O(n)
    for i in range(1, n+1):
        if n%i == 0:
            print(i,end=' ')
    print()

import math
def factors2(n):   # O(sqrt(n))
    i=1 
    while i<=math.sqrt(n):
        if n%i==0:
            if i == n//i:
                print(i,end=' ')
            else:
                print(i,n//i,end=' ')
        i+=1
    print()

def factors3(n):  # O(sqrt(n))
    i = 1
    while i<=math.sqrt(n):
        if n%i==0:
            print(i,end=' ')
        i+=1
    for i in range(int(math.sqrt(n)),0,-1):
        if n%i ==0:
            print(n//i,end=' ')
    print()


def main():
    n = 12
    factors(n)
    factors2(n)
    factors3(n)

main()