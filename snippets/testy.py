
def subArraySum(arr, n, sum_):

	curr_sum = arr[0]
	start = 0

	i = 1
	while i <= n:
		while curr_sum > sum_ and start < i-1:	
			curr_sum = curr_sum - arr[start]
			start += 1
		if curr_sum == sum_:

			print (arr[start: i-1])
			return 1
		if i < n:
			curr_sum = curr_sum + arr[i]
		i += 1

	return 0

# Driver program
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 24

subArraySum(arr, n, sum_)

# This code is Contributed by shreyanshi_arun.
