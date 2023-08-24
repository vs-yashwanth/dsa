def main():
    m,n = list(map(int,input('size: ').split()))
    print(gridtravel(m,n))
    print(gridtravel_gfg(m,n))
    print(gridtravel_memo(m,n))
    print(gridtravel_bottomup(m,n))

def gridtravel(m,n):  # O(2^n)
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    else:
        return gridtravel(m-1,n)+gridtravel(m,n-1)

def gridtravel_gfg(m,n):  # O(2^n)
    if m==1 or n==1:
        return 1
    else:
        return gridtravel_gfg(m-1,n)+gridtravel(m,n-1)

def gridtravel_memo(m,n,d={}):
    key = f'{m},{n}'
    if key in d or reversed(key) in d:
        return d[key]
    if m==1 or n==1:
        return 1
    else:
        #print(d)
        d[key] = gridtravel_memo(m-1,n,d)+gridtravel_memo(m,n-1,d)
        return d[key]

def gridtravel_bottomup(m,n):  # O(mn)
    l = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        l[i][0]=1
    for i in range(n):
        l[0][i]=1
    
    for i in range(1,m):
        for j in range(1,n):
            l[i][j] = l[i-1][j] + l[i][j-1]
    #print(l)
    return l[m-1][n-1]


main()