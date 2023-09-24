import random
import math

# O(n**1/2)

def jump_search(array, val):
    n = len(array)
    k = int(math.sqrt(n))
    r = n-1
    for i in range(0, n, k):
        if array[i] >= val:
            r = i
            break
    l = r-k
    for i in range(l, r+1):
        if a[i] == val:
            return i


if __name__ == '__main__':

    search = jump_search

    n = 6
    a = sorted(random.sample(range(10), n))
    print(a)
    x = sum(random.sample(a, 1))
    print('searching: ', x)
    ind = search(a, x)
    print('index', ind)
    print(a[ind] == x)
