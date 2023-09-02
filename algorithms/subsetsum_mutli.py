# see if a sum is possible with the elements in array. element can be used multiple times.
def main():
    #l=list(map(int,input().split()))
    l = [5,3,4,7]
    #n=int(input('enter num: '))
    n = 7
    
    print(recursion(l,n))
    print(memoized(l,n))
    print(bottomup(l,n))
    print(memoized_show(l,n),s)
    print(memoized_show2(l,n))
    print(bottomup_show(l,n))
    print(memoized_showbest(l,n))
    print(bottomup_showbest(l,n))

def recursion(l,n):  # O(n^m) - O(m)
    if n==0:
        return True
    if n<0:
        return False
    for i in l:
        rem = n-i
        if recursion(l,rem) == True:
            return True
    return False

def memoized(l,n,d={}):  # O(n*m) , O(m)
    if n in d:
        return d[n]   
    if n==0:
        return True
    if n<0:
        return False
    for i in l:
        rem = n-i
        if memoized(l,rem,d) == True:
            d[n] = True
            return d[n]
    d[n]=False
    return d[n]

def bottomup(l,n):  # O(m*n) 
    res = [False]*(n+1)
    res[0] = True
    for i in range(n+1):
        if res[i]:
            for j in l:
                if i+j<=n:
                    res[i+j]=True
    return res[n]


def memoized_show(l,n,d={}):
    if n in d:
        return d[n]   
    if n==0:
        return True
    if n<0:
        return False
    for i in l:
        rem = n-i
        if memoized_show(l,rem,d) == True:
            s.append(i)
            d[n] = True
            return True
    d[n]=False
    return False


def memoized_show2(l,n,d={}):
    if n in d:
        return d[n]   
    if n==0:
        return []
    if n<0:
        return None
    for i in l :
        rem = n-i
        remres = memoized_show2(l,rem,d) 
        if remres is not None:
            d[n]=remres+[i]
            return d[n]
    d[n]=None
    return d[n]

def bottomup_show(l,n):   # O(n*m^2) ; O(m^2)
    res=[None]*(n+1)
    res[0]=[]
    for i in range(n+1):
        if res[i] is not None:
            for j in l:
                if i+j<=n:
                    res[i+j] = res[i]+[j]
    return res[n]

def memoized_showbest(l,n,d={}):  # O(n*m^2), O(m^2 )
    if n in d: 
        return d[n]
    if n==0:
        return []
    if n<0:
        return None
    best=None
    for i in l:
        rem=n-i
        remres = memoized_showbest(l,rem,d)
        if remres is not None:
            current = remres + [i]
            if best is None or len(current)<len(best) :
                best=current
    d[n] = best
    return d[n]

def bottomup_showbest(l,n):
    res = [None]*(n+1)
    res[0] = []
    for i in range(n+1):
         if res[i] is not None:
             for j in l:
                 if i+j<=n:
                     new = res[i]+[j]
                     if res[i+j] is None or len(new)<len(res[i+j]):
                         res[i+j]=new
                        
    return res[n]
        
                
s=[]
main()
        