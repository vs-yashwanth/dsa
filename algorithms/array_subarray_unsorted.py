def main(nums):

    n = len(nums)

    for i in range(n-1):
        if nums[i] > nums[i+1]:
            break
    if i == n-2:
        return 0, []
    for j in range(n-1, 0, -1):
        if nums[j] < nums[j-1]:
            break

    sub_min = float('inf')
    sub_max = -float('inf')

    for k in range(i+1, j+1):
        sub_min = min(sub_min, nums[k])
        sub_max = max(sub_max, nums[k])

    while i > 0 and nums[i-1] > sub_min:
        i -= 1
    while j < n-1 and nums[j+1] < sub_max:
        j += 1

    return j-i+1, nums[i:j+1]


print(main([1, 2, 5, 3, 7, 10, 9, 12]))
print(main([1, 3, 2, 0, -1, 7, 10]))
print(main([1, 2, 3]))
print(main([3, 2, 1]))
