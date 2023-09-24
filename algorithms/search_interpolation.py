import random

# O(log(logn))

def interpolation_search(array, l, r, val):

    if l < r and array[l] <= val <= array[r]:
        n = len(array)
        k = l + ((val - array[l]) * (r - l)) // (array[r] - array[l])

        if array[k] == val:
            return k
        elif array[k] < val:
            return interpolation_search(array, k+1, r, val)
        else:
            return interpolation_search(array, l, k-1, val)
    return -1


if __name__ == '__main__':

    search = interpolation_search

    n = 6
    a = sorted(random.sample(range(10), n))
    print(a)
    x = sum(random.sample(a, 1))
    print('searching: ', x)
    ind = search(a, 0, n-1, x)
    print('index', ind)
    print(a[ind] == x)
