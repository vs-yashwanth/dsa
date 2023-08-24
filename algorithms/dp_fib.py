def main():
    #n=int(input('Enter num: '))
    n=50
    #print(fib(n))
    print(fib_memo(n))
    print(fib_bottomup(n))
    print(fib_bottomup_b(n))
    print(fib_formula(n))

def fib(n):   # O(2**n)
    if n<1:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fib_memo(n,d={}):  
    #print(d)
    if n in d:
        return d[n]
    if n<1:
        return 0
    if n==1:
        return 1
    else:
        d[n]=fib_memo(n-1,d)+fib_memo(n-2,d)
        return d[n]

def fib_bottomup(n):   # O(n), O(1)
    f=[0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    #print(f)
    return f[-1]

def fib_bottomup_b(n):  # O(n), O(1)
    a,b=0,1
    for _ in range(2,n+1):
        c = a+b
        a=b
        b=c
    return b

def fib_formula(n): # O(logn)
    # Fn = {[(√5 + 1)/2] ^ n} / √5 
    import math
    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi, n) / math.sqrt(5))
    

main()
    