def palin(n,k):

    if k%2==0:
        temp = k//2-1
    else:
        temp = k//2
    p = 10**temp + n-1
    print(p,end='')

    if k%2==1:
        p //= 10
    print(str(p)[::-1])


palin(6,6)
    