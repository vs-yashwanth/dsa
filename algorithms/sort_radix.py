import random


def radix_sort(array):
    if not array:
        return array
    max_val = max(array)
    exp = 1
    while max_val / exp >= 1:
        array = counting_sort_digit(array, exp)
        exp *= 10
    return array


def counting_sort_digit(array, exp):
    n = len(array)
    counts = [0] * 10
    out = [-1] * n

    for num in array:
        ind = (num//exp) % 10
        counts[ind] += 1

    for i in range(1, 10):
        counts[i] += counts[i-1]

    for num in reversed(array):
        ind = (num//exp) % 10
        out[counts[ind]-1] = num
        counts[ind] -= 1

    return out


if __name__ == "__main__":
    n = 8
    a = [random.randint(1, 1000) for _ in range(n)]
    print(a)
    s_a = radix_sort(a.copy())
    print(s_a)
    print(s_a == sorted(a))
