# cyclic sort 

def main(nums):
    n = len(nums)
    for i in range(n):
        while nums[i] != n and nums[i] != i:
            j = nums[i]
            nums[i], nums[j] = nums[j], nums[i]

    for i in range(n):
        if i != nums[i]:
            return i

    return n


print(main([4, 0, 3, 1]))
print(main([8, 3, 5, 2, 4, 6, 0, 1]))
