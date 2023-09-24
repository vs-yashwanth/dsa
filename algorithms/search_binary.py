import random

# O(logn)

def binary_search(array, l, r, val):  
    if l <= r:
        mid = (l+r)//2
        if array[mid] == val:
            return mid
        elif array[mid] > val:
            return binary_search(array, l, mid-1, val)
        else:
            return binary_search(array, mid+1, r, val)
    return -1


def binary_search_iter(array, l, r, val):
    n = len(array)
    l = 0
    r = n-1
    while l <= r:
        mid = (l+r)//2
        if array[mid] == val:
            return mid
        elif array[mid] < val:
            l = mid+1
        else:
            r = mid-1
    return -1


if __name__ == '__main__':

    search = binary_search_iter

    n = 6
    a = sorted(random.sample(range(10), n))
    print(a)
    x = sum(random.sample(a, 1))
    print('searching: ', x)
    ind = search(a, 0, n-1, x)
    print('index', ind)
    print(a[ind] == x)
