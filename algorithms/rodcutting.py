# given rod and price list cut to make most profit

def main():
    n=7
    price = {0:0,1:1, 2:5, 3:8, 4:9, 5:10,6:17,7:17,8:20,9:24,10:30}
    print(recursion(n,price))
    print(memoized(n,price))
    print(bottomup(n,price))
    solution(n,price)
    
def recursion(n,price):
    if n<1:
        return 0
    else:
        maxi = -10000
        for i in range(1,n+1):
            p = price[i] + recursion(n-i,price)
            maxi = max(maxi,p)
        return maxi

def memoized(n,price,d={}):
    if n in d:
        return d[n]
    if n<1:
        return 0
    maxi=-10000
    for i in range(1,n+1):
        p = price[i] + memoized(n-i,price,d)
        maxi = max(maxi,p)
    d[n] = maxi
    return d[n]

def bottomup(n,price):
    res = [0]*(n+1)
    
    for i in range(n+1):
        maxi = -10000
        for j in range(i+1):
            p = price[j] + res [i-j]
            maxi = max(maxi,p)
        res[i]=maxi
    #return res
    return res[n]

def solution(n,price):
    res = [0]*(n+1)
    sol = [0]*(n+1)
    for i in range(n+1):
        maxi=-10000
        for j in range(i+1):
            p = price[j]+res[i-j]
            if p>maxi:
                maxi=p
                sol[i]=j
        res[i]=maxi
    print(sol)
    
    
    while n>0:
        print(sol[n],end=' ')
        n-=sol[n]
    
    
main()
        