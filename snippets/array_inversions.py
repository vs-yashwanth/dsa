def naive(A):
    n = len(A)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if A[i]>A[j]:
                count += 1
    return count

def mergesort(A,l,r,temp):
    inv = 0
    if l<r:
        mid = (l+r)//2
        inv += mergesort(A,l,mid,temp)
        inv += mergesort(A,mid+1,r,temp)
        inv += merge(A,l,mid,r,temp)
    return inv

def merge(A,l,m,r,temp):
    inv = 0

    i = l
    j = m+1
    k = l

    while i<m+1 and j<r+1:
        if A[i] <= A[j]:
            #print(temp,i,j,k)
            temp[k] = A[i]
            i += 1
            k += 1
        else:
            temp[k] = A[j]
            j += 1
            k += 1
            inv += m+1 - i
    while i<m+1:
        temp[k] = A[i]
        i += 1
        k += 1
    while j<r+1:
        temp[k] = A[j]
        j += 1
        k += 1
    for i in range(l,r+1):
        A[i] = temp[i]
    
    return inv

if __name__ == '__main__':
    A = [1, 20, 6, 4, 5]
    print(naive(A))
    print(mergesort(A.copy(),0,4,[0]*5))
            
