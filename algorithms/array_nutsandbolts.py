
def match(nuts, bolts,l,r):               # O(nlogn) average,
    if l<r:
        pivot = partition(bolts,l,r,nuts[r])

        partition(nuts,l,r,bolts[pivot])
        match(nuts,bolts,l,pivot-1)
        match(nuts,bolts,pivot+1,r)

def partition(array,l,r,pivot):
    
    i = l
    j = l
    while j<r:
        if array[j]<pivot:
            array[i], array[j] = array[j], array[i]
            i+=1
        elif array[j] == pivot:
            array[r], array[j] = array[j], array[r]
            j-=1
        j += 1
    array[i], array[r] = array[r], array[i]
    return i


nuts = ['@', '#', '$', '%', '^', '&']
bolts = ['$', '%', '&', '^', '@', '#']

match(nuts, bolts, 0, 5)
print("quicksort : ")
print(nuts)
print(bolts)



def match2(nuts,bolts):      # O(n), O(n)
    n = len(nuts)
    m = len(bolts)
    D = {}
    for i,n in enumerate(nuts):
        D[n] = i
    for i in range(m):
        if bolts[i] in D:
            nuts[i] = bolts[i]

nuts = ['@', '#', '$', '%', '^', '&']
bolts = ['$', '%', '&', '^', '@', '#']


match2(nuts, bolts)
print("hashmap : ")
print(nuts)
print(bolts)
