import random


def bubble_sort(a):
    n = len(a)
    for i in range(n):
        flag = False
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = True
        if not flag:
            break
    return a


if __name__ == '__main__':

    a = list(random.sample(range(1, 9), 6))

    print(a)
    s_a = bubble_sort(a.copy())
    print(s_a)
    print(s_a == sorted(a))
