
from random import randint 

def randomPartition(arr, l, r): 
	n = r - l + 1
	pivot = randint(1, 100) % n 
	arr[l + pivot], arr[r] = arr[l + pivot], arr[r] 
	return partition(arr, l, r) 

def kthSmallest(arr, l, r, k): 

	# If k is smaller than 
	# number of elements in array 
	if (k > 0 and k <= r - l + 1): 

		pos = randomPartition(arr, l, r) 

		# If position is same as k 
		if (pos - l == k - 1): 
			return arr[pos] 
			
		# If position is more, recur for left subarray 
		if (pos - l > k - 1): 
			return kthSmallest(arr, l, pos - 1, k) 

		# Else recur for right subarray 
		return kthSmallest(arr, pos + 1, r, 
						k - pos + l - 1) 

	# If k is more than number of elements in array 
	return 10**9

def partition(arr, l, r): 
	x = arr[r] 
	i = l 
	for j in range(l, r): 
		if (arr[j] <= x): 
			arr[i], arr[j] = arr[j], arr[i] 
			i += 1

	arr[i], arr[r] = arr[r], arr[i] 
	return i 

# Driver Code 
arr = [12, 3, 5, 7, 4, 19, 26] 
n = len(arr) 
k = 3
print("K'th smallest element is", 
	kthSmallest(arr, 0, n - 1, k)) 


