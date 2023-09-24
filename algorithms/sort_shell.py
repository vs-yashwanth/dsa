import random
# generalized insertion sort - goes back gap steps instead of 1


def shell_sort(a):
    n = len(a)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            key = a[i]
            j = i
            while j >= gap and a[j-gap] > key:
                a[j] = a[j-gap]
                j -= gap
            a[j] = key
        gap //= 2
    return a


if __name__ == '__main__':

    a = list(random.sample(range(1, 9), 8))
    a = [4, 6, 7, 3, 2, 5, 8, 1]
    print(a)
    s_a = shell_sort(a.copy())
    print(s_a)
    print(s_a == sorted(a))
