

def sort01(A):
    n = len(A)
    i = 0
    j = n-1
    while i<j:
        if A[i] == 0:
            i += 1
        else:
            A[i], A[j] = A[j], A[i]
            j -= 1
    return A 




if __name__ == '__main__':

    fn = sort01

    arr = [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1]
    print(arr)
    arr_s = fn(arr)
    print(arr_s)
    print(arr_s == sorted(arr))
