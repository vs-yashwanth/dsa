
def mergeArrays(a1,a2,n1,n2):

    out = [0]*(n1+n2)
    i = j = k =0
    while i<n1 and j<n2:
        if a1[i] < a2[j]:
            out[k] = a1[i]
            i += 1
       
        else:
            out[k] = a2[j]
            j += 1

        k += 1
    
    while i<n1:
        out[k] = a1[i]
        i+=1
        k+=1
    while j<n2:
        out[k] = a2[j]
        j+=1
        k+=1
    
    print(out)

arr1 = [1, 3, 5, 7]
n1 = len(arr1)
 
arr2 = [2, 4, 6, 8]
n2 = len(arr2)
mergeArrays(arr1, arr2, n1, n2)