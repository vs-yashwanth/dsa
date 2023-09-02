def main():
    n=int(input('enter n: '))
    for i in range(n):
        print(catalan(i),end=' ')
    print()

    cat= dynamic_catalan(n)
    print(cat)

def catalan(n):
    if n<=1:
        return 1
    else:
        c=0
        for i in range(n):
            c += catalan(i)*catalan(n-i-1)
        return c

def dynamic_catalan(n):
    cat=[0]*(n)
    cat[0]=1
    cat[1]=1
    for i in range(2,n):
        for j in range(i):
            cat[i]+=cat[j]*cat[i-j-1]
    return cat
    
main()