import random

# find the minimum element in each iteration and put it
# in its place

def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_ind = i
        for j in range(i+1, n):
            if a[j] < a[min_ind]:
                min_ind = j
        a[i], a[min_ind] = a[min_ind], a[i]
    return a


if __name__ == '__main__':

    a = list(random.sample(range(1, 9), 6))


    print(a)
    s_a = selection_sort(a.copy())
    print(s_a)
    print(s_a == sorted(a))
