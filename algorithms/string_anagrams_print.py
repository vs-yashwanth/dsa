def permute(a,l,r):     # O(n*n!)
    if l == r:
        print(''.join(a))
    else:
        for i in range(l,r+1):
            a[l],a[i] = a[i],a[l]
            permute(a,l+1,r)
            a[l],a[i] = a[i],a[l]

if __name__ == '__main__':
    s = 'abc'
    permute(list(s),0,len(s)-1)