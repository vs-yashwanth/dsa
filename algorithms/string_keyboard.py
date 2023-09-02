def recursive(N):
    if N<7:
        return N
    maxi = 0
    for i in range(N-3,0,-1):
        cur = (N-i-1)*optimal(i)
        maxi = max(maxi, cur)
    return maxi

def optimal(n):
    if n<7:
        return n
    out = [0]*(n)
    for i in range(1,7):
        out[i-1] = i
    for n in range(7,n+1):
        out[n-1] = 0
        for b in range(n-3,0,-1):
            cur = (n-b-1)*out[b-1]
            if cur > out[n-1]:
                out[n-1] = cur
            
    return out[n-1]


for n in range(1, 21):
    print('Maximum Number of As with ', n, 'keystrokes is ', optimal(n))
