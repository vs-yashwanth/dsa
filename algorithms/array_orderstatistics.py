import heapq as pq
import random

def kthsmallest(A,n,k):   # O(nlogn)
    A.sort()
    return A[k-1]

def kthsmall_heap(A,k):  # O(n + klogn)
    pq.heapify(A)
    for _ in range(k):
        o = pq.heappop(A)
    return o

def quickselect(A,l,r,k):   # O(n) expected ; O(n**2) worst
    if k>0 and k<=r-l+1:
        pos = rand_partition(A,l,r,k)
        if pos-l == k-1:
            return A[pos]
        elif pos-l > k-1:
            return quickselect(A,l,pos-1,k)
        else:
            return quickselect(A,pos+1,r,k-pos+l-1)
    return -1

def rand_partition(A,l,r,k):
    x = random.randint(l,r)
    A[x],A[r] = A[r],A[x]
    return partition(A,l,r,k)

def partition(A,l,r,k):

    pivot = A[r]
    i = l
    for j in range(l,r):
        if A[j] <= pivot:
            A[i],A[j] = A[j],A[i]
            i += 1
    A[r],A[i] = A[i],A[r]
    return i

def MedianofMedians(A,l,r,k):  # O(n) worst
	n = r-l+1
	if k>0 and k<=n:
		medians = []
		i = 0
		while i<n//5:
			medians.append(get_median(A,l+i*5,5))
			i += 1
		if i*5 < n:
			medians.append(get_median(A,l+i*5,n%5))
			i += 1
		if i == 1:
			medofmed = medians[i-1]
		else:
			medofmed = MedianofMedians(medians,0,i-1,i//2)
		
		pos = new_partition(A,l,r,medofmed)

		if pos-l == k-1:
			return A[pos]
		elif pos-l > k-1:
			return MedianofMedians(A,l,pos-1,k)
		else:
			return MedianofMedians(A,pos+1,r,k+i-pos-1)
	
	else:
		return -1

def new_partition(A,l,r,medofmed):
	for i,e in enumerate(A):
		if e == medofmed:
			A[i],A[r] = A[r], A[i]
	
	pivot = A[r]
	i = l
	for j in range(i,r):
		if A[j]<=A[r]:
			A[i],A[j] = A[j],A[i]
			i += 1
	A[r],A[i] = A[i],A[r]
	return i

def get_median(A,l,n):
	l = A[l:l+n]
	l.sort()
	return l[n//2]



if __name__=='__main__':
    arr = [12, 3, 5, 7, 19]
    n = len(arr)
    k = 2
    print( kthsmallest(arr.copy(), n, k))
    print(kthsmall_heap(arr.copy(),k))
    print(quickselect(arr.copy(),0,4,k))
    print(MedianofMedians(arr.copy(),0,4,k))
    