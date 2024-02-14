# Find the First K Missing Positive Numbers

def k_missing(nums, k):  # O(n+k), O(k)
    n = len(nums)
    missing = []
    over_range_numbers = set()
    for i in range(n):
        while nums[i] != i+1 \
                and 1 < nums[i] <= n \
                and nums[i] != nums[nums[i]-1]:
            j = nums[i]
            nums[i], nums[j-1] = nums[j-1], j

    for i in range(n):
        if nums[i] != i+1 and len(missing) != k:
            missing.append(i+1)
            if nums[i] >= n:
                over_range_numbers.add(nums[i])

    out_range = n+1
    while len(missing) < k:
        if out_range not in over_range_numbers:
            missing.append(out_range)
        out_range += 1

    return missing


print(k_missing([3, -1, 4, 8, 5], k=3))
print(k_missing([2, 3, 4], k=3))
print(k_missing([-2, -3, 4], k=2))

# cyclic sort
