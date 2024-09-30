# string matching
def main():
    t='AABAACAADAABAAABAA'
    p='AABA'
    print(naive_match(t,p))
    print(rabin_karp(t,p,101))
    print(KMP(t,p))
    print(finite_automata(t,p))

def naive_match(t,p):  # O(m*(n-m+1))
    matches=[]
    n,m=len(t),len(p)
    for s in range(0,n-m+1):
        if p==t[s:s+m]:
            matches.append(s)
    return matches
# there is naive_match in O(n) if p is all unique

def rabin_karp(T,P,q,d=256):  # O(n) expected, O(m*(n-m+1)) worst
    sol=[]
    n,m = len(T),len(P)
    h = (10**(m-1))%q
    p = 0
    t = 0
    for i in range(m):
        p = (d*p + ord(P[i]))%q
        t = (d*t + ord(T[i]))%q
    for i in range(n-m+1):
        if p==t:
            for j in range(m):
                if P[j] != T[i+j]:
                    break
                else:
                    j+=1
            if j==m:
                sol.append(i)
    if i<n-m:
        t = (d*(t-ord(T[i])*h) + ord(T[i+m])) %q
        if t<0:
            t+=q
    return sol
        
def KMP(T,P):
    sol = []
    m,n = len(P), len(T)
    pi = kmp_prefix(P)
    i = j = 0
    
    while i<n:
        if P[j] == T[i]:
            i+=1
            j+=1
        if j==m:
            sol.append(i-j)
            j = pi[j-1]
        elif i<n and P[j] != T[i]:
            if j!=0:
                j = pi[j-1]
            else:
                i+=1
    return sol

def kmp_prefix(P):
    m = len(P)
    pi = [0]*m
    l = 0
    i = 1
    
    while i < m:
        if P[i] == P[l]:
            l+=1
            pi[i] = l
            i+=1
        else:
            if l!=0:
                l = pi[l-1]
            else:
                pi[i] = 0
                i+=1
                
    return pi
    
def finite_automata(T,P):
    return 'finite automata loading...'
main()