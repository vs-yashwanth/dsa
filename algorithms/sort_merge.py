import random

def merge_sort(a,l,r):
    if l<r:
        m = (l+r)//2
        merge_sort(a,l,m)
        merge_sort(a,m+1,r)
        merge(a,l,m,r)

def merge(a,l,m,r):
    n1 = m-l+1
    n2 = r-m
    l1 = [a[l+i] for i in range(n1)]
    l2 = [a[m+1+j] for j in range(n2)]
    i = j = 0
    k = l
    while i<n1 and j<n2:
        if l1[i] <= l2[j]:
            a[k] = l1[i]
            i += 1
        else:
            a[k] = l2[j]
            j += 1
        k += 1
    while i<n1:
        a[k] = l1[i]
        i += 1
        k += 1
    while j<n2:
        a[k] = l2[j]
        j += 1
        k += 1


if __name__ == '__main__':
    n = 6
    a = list(random.sample(range(1, 10), n))

    print(a)
    a_s = a.copy()
    merge_sort(a_s, 0, n - 1)
    print(a_s)
    print(a_s == sorted(a))
