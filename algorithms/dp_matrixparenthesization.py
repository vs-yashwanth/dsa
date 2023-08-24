# matrix paranthesiaztion
import numpy as np
def main():
    a=[30,35,15,5,10,20,25]
    n=len(a)
    print(cost_recursion(a,1,n-1))
    print(cost_memoized(a,1,n-1))
    c,s=cost_bottomup(a)
    print(c)
    solution(s,1,n-1)


def cost_recursion(a,i,j):  # catalan, O(2^n)
    if i==j:
        return 0
    mini = 1000000
    for k in range(i,j):
        c=cost_recursion(a,i,k)+\
            cost_recursion(a,k+1,j) + \
                a[i-1]*a[k]*a[j]
        if c<mini:
            mini=c
    return mini

def cost_memoized(a,i,j,d={}):
    key=f'{i},{j}'
    if key in d or key[::-1] in d:
        return d[key]
    if i==j:
        return 0
    mini = 10000000
    for k in range(i,j):
        q = cost_memoized(a,i,k,d) + cost_memoized(a,k+1,j,d) + \
            a[i-1]*a[k]*a[j]
        if q<mini:
            mini = q
    d[key]=mini
    return d[key]
    
    

def cost_bottomup(p):    # O(n^3); O(n^2)
    n=len(p)-1
    m=[[10000000 for i in range (n)] for j in range(n)]
    for i in range(n):
        m[i][i]=0
    s= [[0 for i in range(n)] for j in range(n)]
    
    for l in range(2,n+1):
        for i in range(1,(n-l+1)+1):
            j = (i+l-1)
            for k in range(i,j):
                #print(l,i,j,k)
                q = m[i-1][k-1] + m[k][j-1] + p[i-1]*p[k]*p[j]
                if q<m[i-1][j-1]:
                    m[i-1][j-1]=q
                    s[i-1][j-1]=k
    #return m[0][n-1],s[0][n-1]
    #m,s=cost_bottomup(a)
    #print(np.array(m))
    #print(np.array(s))
    #return m,s
    return m[0][n-1],s

def solution(s,i,j):
    if i==j:
        print('A{}'.format(i),end=" ")
    else:
        print('(',end=' ')
        solution(s,i,s[i-1][j-1])
        solution(s,s[i-1][j-1]+1,j)
        print(")",end=' ')

main()
            
        