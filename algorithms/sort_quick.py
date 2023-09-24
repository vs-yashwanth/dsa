import random


def quick_sort(a, l, r):
    if l < r:
        m = partition(a, l, r)
        quick_sort(a, l, m-1)
        quick_sort(a, m+1, r)
    return a


def partition(a, l, r):
    pivot = a[r]
    j = l-1
    for i in range(l, r):
        if a[i] < pivot:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[j+1], a[r] = a[r], a[j+1]
    return j+1


def rand_partition(a, l, r):
    rand_r = random.randint(l, r)
    a[r], a[rand_r] = a[rand_r], a[r]
    return partition(a, l, r)


if __name__ == '__main__':
    n = 6
    a = list(random.sample(range(1, 9), n))

    print(a)
    a_s = a.copy()
    a_s = quick_sort(a_s, 0, n-1)
    print(a_s)
    print(a_s == sorted(a))
