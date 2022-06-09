import random

inv = 0
def main():
    # print(random.sample.__doc__)
    #a = list(random.sample(range(1, 10), 5))
    a=[1, 20, 6, 4, 5]

    print(a)
    n = 5

    mergesort(a, 0, n - 1)
    print(a)
    print(a == sorted(a))
    print('inv =',inv)


def mergesort(a, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        mergesort(a, l, m)
        mergesort(a, m + 1, r)
        merge(a, l, m, r)


def merge(a, l, m, r):
    global inv
    n1 = m - l + 1
    n2 = r - m
    l1 = [0] * n1
    l2 = [0] * n2
    for i in range(n1):
        l1[i] = a[l + i]
    for i in range(n2):
        l2[i] = a[m + 1 + i]
    i = j = 0
    k = l

    while i < n1 and j < n2:
        if l1[i] <= l2[j]:
            a[k] = l1[i]
            i += 1
        else:
            a[k] = l2[j]
            j += 1
            inv+=n1-i
        k += 1
    while i < n1:
        a[k] = l1[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = l2[j]
        j += 1
        k += 1
main()
