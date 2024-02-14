
def find_missing(nums):  # O(n)

    for i in range(len(nums)):
        while nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
            j = nums[i]
            nums[i], nums[j-1] = nums[j-1], j

    missing = []
    for i in range(len(nums)):
        if nums[i] != i+1:
            missing.append(i+1)

    return missing


print(find_missing([2, 3, 1, 8, 2, 3, 5, 1]))
print(find_missing([2, 4, 1, 2]))
print(find_missing([2, 3, 2, 1]))


# cyclic sort
