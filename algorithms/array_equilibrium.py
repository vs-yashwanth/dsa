
def equi_naive(A):

    for i in range(len(A)):
        if sum(A[:i]) == sum(A[i+1:]):
            print(i,end=' ')
    print()

def equi(A):
    rightsum = sum(A)
    leftsum = 0
    for i in range(len(A)):
        rightsum -= A[i]
        if leftsum == rightsum:
            print(i,end=' ')
        leftsum += A[i]
    print()


arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
equi_naive(arr)
equi(arr)