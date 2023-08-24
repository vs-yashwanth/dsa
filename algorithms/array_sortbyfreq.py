def freq_sort_easy(A):
    return sorted(A,key=A.count,reverse=True)


def freq_sort(A):
    D = {}
    for i in A:
        if i not in D:
            D[i] = 0
        D[i] += 1
    A = []
    E = {}
    for i in D:
        if D[i] not in E:
            E[D[i]] = []
        E[D[i]].append(i)
    D = E

    for i in sorted(D,reverse=True):
        for j in D[i]:
            A+=[j]*i
    
    return A



l = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 5, 5, 5, 4, 4, 4, 4, 4, 4]
print(freq_sort(l))
print(freq_sort_easy(l))