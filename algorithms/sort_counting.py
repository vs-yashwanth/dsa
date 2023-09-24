# sorting in linear time
# counting sort
import random


def counting_sort(array):
    k = max(array)
    n = len(array)
    counts = [0]*(k+1)
    out = [-1]*n
    for val in array:
        counts[val] += 1
    # each element in c has the count of elements in a
    # if there 3 4's in a, c[4]=3

    for j in range(1, k+1):
        counts[j] += counts[j-1]

    # each element in c represents the number of elements <= its
    # index value in a
    # if c[4]=10, then there are 10 elements in a that are less than
    # or equal to 4.
    for val in array:
        out[counts[val]-1] = val
        counts[val] -= 1
    return out


if __name__ == '__main__':
    n = 6
    a = list(random.sample(range(1, 9), n))
    print(a)
    a_s = a.copy()
    a_s = counting_sort(a_s)
    print(a_s)
    print(a_s == sorted(a))
