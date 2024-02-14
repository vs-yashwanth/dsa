

def main(nums):  # O(n)
    n = len(nums)
    for i in range(n):
        while nums[i] != i+1 and 0 < nums[i] <= n:
            j = nums[i]
            nums[i], nums[j-1] = nums[j-1], j

    for i in range(n):
        if nums[i] != i+1:
            return i+1


print(main([-3, 1, 5, 4, 2]))
print(main([3, -2, 0, 1, 2]))
print(main([3, 2, 5, 1]))

# cyclic sort
