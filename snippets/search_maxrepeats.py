def main():
    a = [1,2,3,1,2,4,1]
    print(find(a))
    print(find2(a))
    print(find3(a))
    print(find4(a))

def find(a):    # O(n^2)
    n = len(a)
    maxi = (0,0)
    for i in range(n):
        count = 1
        for j in range(i+1, n):
            if a[i] == a[j]:
                count += 1
        if count > maxi[1]:
            maxi = (a[i], count)
    return maxi

def find2(a):     # O(nlogn)
    n = len(a)
    maxi = (0,0)
    a.sort()
    i = 0
    count = 1
    while i+1 < n:
        if a[i] == a[i+1]:
            count += 1
        elif a[i] != a[i+1]:
            if count > maxi[1]:
                maxi = (a[i], count)
            count = 1
        i += 1
    return maxi



def find3(a):   # O(n), O(n)
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    maxi = max(d, key = lambda x : d[x])
    return (maxi, d[maxi])

def find4(a):   # O(n)
    n = len(a)
    for i in range(n):
        a[a[i]%n] += n
    maxi = out = 0
    for i in a:
        if maxi < i//n:
            maxi = i//n
            out = (i%n, maxi)
    return out

main()


        