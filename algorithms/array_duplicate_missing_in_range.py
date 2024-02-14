

def main(nums):  # O(n)

    for i in range(len(nums)):
        while nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
            j = nums[i]
            nums[i], nums[j-1] = nums[j-1], j
    
    for i in range(len(nums)):
        if nums[i] != i+1:
            return nums[i], i+1
    


print(main([3, 1, 2, 5, 2]))
print(main([3, 1, 2, 3, 6, 4]))


# cyclic sort