# sees and prints the way to generate given string with given word list
def main():
    s='abcdef'
    #words=['purp','p','ur','le','purpl']
    words = ['ab','abc','cd','def','abcd','ef','c']
    print(ifrecursion(s,words))
    print(ifmemoized(s,words))
    print(ifbottomup(s,words))
    print(numways_memoized(s,words))
    print(numways_bottomup(s,words))
    print(showways(s,words))
    print(showways_memoized(s,words))
    print(showways_bottomup(s,words))

def ifrecursion(s,words):  # O(m*n^m), O(m^2)
    if s=='':
        return True
    
    for w in words:
        if s.find(w)==0:
            if ifrecursion(s.replace(w,''),words) == True:
                return True
    return False

def ifmemoized(s,words,d={}): # O(n*m^2), O(m^2)
    if s in d:
        return d[s]
    if s=='':
        return True
    for w in words:
        if s.find(w)==0:
            if ifmemoized(s.replace(w,''),words):
                d[s]= True
                return d[s]
    d[s]=False
    return d[s]

def ifbottomup(s,words):  # O(n*m^2), O(m)
    n = len(s)
    res = [False]*(n+1)
    res[0] = True
    for i in range(n+1):
        if res[i]==True:
            for w in words:
                if i<n and w[0]==s[i] and i+len(w)<=n:
                    res[i+len(w)]=True
    return res[n]
    

def numways_memoized(s,words,d={}):  # O(n*m^2), O(m^2)
    if s in d:
        return d[s]
    if s=='':
        return 1
    total=0
    for w in words:
        if s.find(w)==0:
            total += numways_memoized(s.replace(w,''),words,d)
    
    d[s]=total
    return d[s]

def numways_bottomup(s,words):   # 
    n=len(s)
    res = [0]*(n+1)
    res[0]=1
    for i in range(n+1):
        if res[i]!=0:
            for w in words:
                if i<n and w[0] == s[i] and i+len(w)<=n:
                    res[i+len(w)]+=res[i]
    return res[n]

def showways(s,words):
    if s=='':
        return [[]]
    total =[]
    for w in words:
        if s.find(w)==0:
            sufways = showways(s.replace(w,''),words)
            sways = [[w]+a for a in sufways]
            total+=sways
    return total

def showways_memoized(s,words,d={}):  # O(n^m) ; O(m)
    if s in d:
        return d[s]
    if s=='':
        return [[]]
    total=[]
    for w in words:
        if s.find(w)==0:
            sufways = showways_memoized(s.replace(w,''),words,d)
            sways = [ [w]+a for a in sufways]
            total += sways
    d[s] = total
    return d[s]

def showways_bottomup(s,words):  # O(n^m) ; O(n^m)
    n=len(s)
    res=[[] for _ in range(n+1)]
    res[0]=[[]]
    for i in range(n+1):
        if res[i] != []:
            for w in words:
                if i<n and w[0]==s[i] and i+len(w)<=n:
                    sways = [[w]+a for a in res[i]]
                    res[i+len(w)] += sways
    return res[n]
            
    
    
main()