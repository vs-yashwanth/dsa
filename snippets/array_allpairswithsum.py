def allpairs(A, target):
    out = []
    D = {}
    for i in A:
        pot = target-i
        if pot in D:
            for _ in range(D[pot]):
                out.append((i,pot))
        if i not in D:
            D[i] = 0
        D[i] += 1
    return out


arr = [ 1, 5, 7, -1, 5 ]
n = len(arr)
sum = 6
print(allpairs(arr,sum))