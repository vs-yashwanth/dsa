def relative_sort(s1,s2):  # O(n+m+qlogq), O(n)

    D = {}
    for i in s1:
        if i not in D:
            D[i] = 0
        D[i] += 1
    s1 = []
    for i in s2:
        if i in D:
            s1 += [i]*D[i]
            D.pop(i)
    s1 += sorted(D)
    return s1

if __name__ == "__main__":
    arr1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
    arr2 = [2, 1, 8, 3]
    print(relative_sort(arr1, arr2))


