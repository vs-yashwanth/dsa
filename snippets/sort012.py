
def sort012(A,n):

    i = 0
    k = 0
    j = n - 1

    while k<j:
        if A[k] == 0:
            A[i],A[k] = A[k],A[i]
            i += 1
            k += 1
        elif A[k] == 2:
            A[j],A[k] = A[k],A[j]
            j -= 1
        else:
            k+=1

arr = [2, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 2]
arr_size = len(arr)
sort012( arr, arr_size)
print(arr)