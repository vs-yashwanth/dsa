import random
def main():
    # print(random.sample.__doc__)
    a = list(random.sample(range(1, 10), 6))

    print(a)

    shellsort(a)
    print(a)
    print(a == sorted(a))

def shellsort(a):
    n = len(a)
    gap = n // 2
    while gap > 0:
        i = 0
        j = gap
        while j < n:
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
            k = i
            while k - gap > -1:
                if a[k-gap] > a[k]:
                    a[k], a[k-gap] = a[k-gap], a[k]
                k -= 1
        gap //=2


main()