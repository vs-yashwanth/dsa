def diff(A,n,m):

	if m==0 or n==0:
		return 0
	if n<m:
		return -1
	A.sort()
	mini = A[-1] - A[0]
	for i in range(n-m+1):
		mini = min(mini, A[i+m-1] - A[i])
	
	return mini


if __name__ == "__main__":
    arr = [12, 4, 7, 9, 2, 23, 25, 41,30, 40, 28, 42, 30, 44, 48,43, 50]
    m = 7 # Number of students
    n = len(arr)
    print("Minimum difference is", diff(arr, n, m))