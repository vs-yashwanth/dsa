# returns longest palindrome subsequence in string
# can also split into two and solve the lcs
# can also make duplicate reverse and solve the lcs

def main():
    s='z234a5abbba54a32z'
    n=len(s)
    #print(recursive(s,0,n-1))
    print(memoized(s,0,n-1))
    print(bottomup(s))

def recursive(s,i,j):
    if j<i:
        return 0
    if i==j:
        return 1
    if s[i]==s[j]:
        return 2 + recursive(s,i+1,j-1)
    else:
        return max(recursive(s,i+1,j),recursive(s, i, j-1))

def memoized(s,i,j,d={}):
    key = f'{i},{j}'
    if key in d:
        return d[key]
    if j<i:
        d[key]=0
    elif i==j:
        d[key]=1
    elif s[i]==s[j]:
        d[key]=2+memoized(s,i+1,j-1,d)
    else:
        d[key]=max(memoized(s, i+1, j,d), memoized(s, i, j-1, d))
    return d[key]

def bottomup(s):  # O(n^2)
    n=len(s)
    c=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        c[i][i]=1
    for l in range(2,n+1):
        for i in range(n-l+1):
            j=i+l-1
            if s[i]==s[j] and l==2:
                c[i][j]=2
            elif s[i]==s[j]:
                c[i][j] = 2+c[i+1][j-1]
            else:
                c[i][j] = max(c[i+1][j], c[i][j-1])
    
    #printing
    s2=s[::-1]
    i,j=len(s)-1,len(s2)-1
    w=''
    while i>=0 and j>=0:
        if s[i]==s2[j]:
            w+=s[i]
            i-=1
            j-=1
        elif c[i-1][j]>c[i][j-1]:
            i-=1
        else:
            j-=1
    w=w[::-1]
    
    return c[i][j], w
    
    
main()