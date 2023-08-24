# longest increasing subsequence
# can also take sorted(list) as 2nd string and do LCS

#global maxi 
maxi = 1 

def main():
    l= [10, 22, 9, 33, 21, 50, 41, 60]
    #l=[1,2,3,4,5,6,7,8,10]
    n=len(l)
    print(recursion(l,n))
    print(bottomup(l))
    print(bottomup_lcs(l))
    print(best(l))

def recursion(l,n):
    #global maxi
    
    if n==1:
        return 1
    maxhere = 1
    for i in range(1,n):
        res = recursion(l,i)
        if l[i-1]<l[n-1] and res+1>maxhere:
            maxhere=res+1
    #maxi=max(maxi,maxhere)
    return maxhere

def bottomup(l):   # O(n^2) ; O(n)
    n=len(l)
    s=[1]*n
    
    for i in range(1,n):
        for j in range(i):
            if l[i]>l[j] and s[i]<s[j]+1:
                s[i]=s[j]+1
    #print(s)
    return max(s)

def bottomup_lcs(l):  # O(m*n = n^2) ; O(n^2) 
    a=l.copy()
    b=list(sorted(set(a)))
    #print(a,b)
    m,n=len(a),len(b)
    c = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m):
        for j in range(n):
            if a[i]==b[j]:
                c[i][j]= 1+c[i-1][j-1]
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
    i=m-1;j=n-1
    w=[]
    while i>=0 and j>=0:
        if a[i]==b[j]:
            w.append(a[i])
            i-=1
            j-=1
        elif c[i-1][j]>c[i][j-1]:
            i-=1
        else:
            j-=1
    print(w[::-1])
    
    return c[m-1][n-1]

def best(l):
    return 'O(nlogn) solution loading...'
    
    
            
    
main()