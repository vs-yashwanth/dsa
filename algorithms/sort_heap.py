import random
def left(i):
	return 2*i
def right(i):
	return 2*i+1
def parent(i):
	return i//2
def maxheapify(A,i):
	l=left(i)
	r=right(i)
	if l<len(A) and A[l]>A[i]:
		largest=l
	else:
		largest=i
	if r<len(A) and A[r]>A[largest]:
		largest=r
	if largest!=i:
		A[i],A[largest] = A[largest],A[i]
		A=maxheapify(A,largest)
	return A

def buildheap(A):
	for i in range(len(A)//2,-1,-1):
		A=maxheapify(A,i)
	return A

def heapsort(A):
    A=buildheap(A)
    #print('heap',A)
    heapsize=len(A)
    for i in range(len(A)-1,0,-1):
        A[0],A[i] = A[i], A[0]
        heapsize-=1
        r=A[heapsize:]
        #print('r',r)
        b=maxheapify(A[:heapsize],0)
        A=b+r
    return A
def main():
    A=random.sample(range(100),50)
    print(A)
    A=(heapsort(A))
    print(A)
    print(A==sorted(A))

main()