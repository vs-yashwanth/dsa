import random

def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a


if __name__ == '__main__':

    a = list(random.sample(range(1, 10), 6))
    print(a)
    s_a = insertion_sort(a.copy())
    print(s_a)
    print(s_a == sorted(a))
