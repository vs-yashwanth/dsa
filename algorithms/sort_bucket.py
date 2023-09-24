import random
from sort_insertion import insertion_sort


def bucket_sort(array):

    buckets = [[] for _ in range(10)]

    for val in array:
        ind = int(val*10)
        buckets[ind].append(val)

    for i in range(10):
        buckets[i] = insertion_sort(buckets[i])

    out = []
    for bucket in buckets:
        out.extend(bucket)

    return out


if __name__ == '__main__':
    n = 6
    a = [random.random() for _ in range(n)]
    print(a)
    a_s = a.copy()
    a_s = bucket_sort(a_s)
    print(a_s)
    print(a_s == sorted(a))
