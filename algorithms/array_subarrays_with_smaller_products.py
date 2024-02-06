

def main(nums, target):
    out = []
    for i in range(len(nums)):
        running_total = nums[i]
        j = i+1
        while running_total < target:
            out.append(nums[i:j])
            if j >= len(nums):
                break
            running_total *= nums[j]
            j += 1

    return out


print(main([2, 5, 3, 10], 30))
print(main([8, 2, 6, 5], 50))

# [2], [2, 5], [5], [5, 3], [3],[10]
