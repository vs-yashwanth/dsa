# longest common subsequence in increasing order
def main():
    a="z234a5abbba54a32z"
    b=a[::-1]
    m,n = len(a),len(b)
    print("recurion:", recursion(a,b,m,n))
    print("memoized:",memoized(a,b,m,n))
    c,s = bottomup(a,b)
    print('bottomup:',c)
    build(a,s,m-1,n-1)
    

def recursion(a,b,i,j): # O(2^m)
    
    if i==0 or j==0:
        return 0
    elif a[i-1]==b[j-1]:
        return 1 + recursion(a,b,i-1,j-1)
    else:
        return max(recursion(a, b, i-1, j), recursion(a, b, i, j-1))

def memoized(a,b,i,j,d={}):  #O(m*n)
    key = f'{i},{j}'
    if key in d :
        return d[key]
    if i==0 or j==0:
        return 0
    elif a[i-1]==b[j-1]:
        d[key] = 1 + memoized(a, b, i-1, j-1)
        return d[key]
    else:
        d[key] = max( memoized(a, b, i-1, j) , memoized(a, b, i, j-1))
        return d[key]
    
    
def bottomup(a,b):   # O(m*n)
    m,n=len(a),len(b)
    c = [[0 for i in range(n+1)] for j in range(m+1)]
    s = [[0 for i in range(1,n+1)] for j in range(1,m+1)]
    for i in range(m):
        for j in range(n):            
            if a[i]==b[j]:
                c[i][j] = 1 + c[i-1][j-1]
                s[i][j] = 'D'
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j] = c[i-1][j]
                s[i][j] = 'U'
            else:
                c[i][j]=c[i][j-1]
                s[i][j] = 'L'
    i=m-1; j=n-1
    w=''
    print(c)
    # printing
    while i>-1 and j>-1:
        if a[i]==b[j]:
            w+=a[i]
            i-=1
            j-=1
        elif c[i-1][j] > c[i][j-1]:
            i-=1
        else:
            j-=1
    print(w[::-1])
    
    return c[m-1][n-1], s
    
def build(a,s,i,j):
    if i==-1 or j==-1:
        return
    if s[i][j] == 'D':
        build(a,s,i-1,j-1)
        print(a[i],end='')
    elif s[i][j] == 'U':
        build(a,s,i-1,j)
    else:
        build(a,s,i,j-1)
        

main()
    