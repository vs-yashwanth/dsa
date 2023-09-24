
def sort1(a):    # counting sort
    n = len(a)
    max_val = max(a)
    counts = [0]*(max_val+1)
    out = [-1]*n

    for num in a:
        counts[num] += 1
    for i in range(1, max_val+1):
        counts[i] += counts[i-1]

    for num in a:
        out[counts[num]-1] = num
        counts[num] -= 1

    return out


def sort2(a):
    n = len(a)
    i = j = 0
    k = n-1
    while j <= k:
        if a[j] == 0:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
        elif a[j] == 2:
            a[j], a[k] = a[k], a[j]
            k -= 1
        elif a[j] == 1:
            j += 1

    return a


if __name__ == '__main__':

    fn = sort2

    arr = [2, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 2]
    print(arr)
    arr_s = fn(arr)
    print(arr_s)
    print(arr_s == sorted(arr))
