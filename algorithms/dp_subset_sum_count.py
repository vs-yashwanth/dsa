# find the total number of subsets whose sum is equal to a given number ‘S’.

def bruteforce(nums, target):   # O(2**n), O(n)

    def backtrack(cur_sum, i):
        if cur_sum == 0:
            return 1
        if i == len(nums) or cur_sum < 0:
            return 0
        return backtrack(cur_sum, i+1) + backtrack(cur_sum - nums[i], i+1)

    return backtrack(target, 0)


def topdown(nums, target):      # O(n * target), O(n * target)
    memo = {}

    def dp(cur_sum, i):
        if cur_sum == 0:
            return 1
        if i == len(nums) or cur_sum < 0:
            return 0
        if (i, cur_sum) in memo:
            return memo[(i, cur_sum)]
        memo[(i, cur_sum)] = dp(cur_sum, i+1) + dp(cur_sum - nums[i], i+1)
        return memo[(i, cur_sum)]

    return dp(target, 0)


def bottomup(nums, target):       # O(n * target), O(n)

    dp = [0 for _ in range(target+1)]
    dp[0] = 1

    for num in nums:
        for t in range(target, -1, -1):
            if num <= t:
                dp[t] += dp[t-num]
    return dp[-1]


if __name__ == '__main__':

    subset_sum_count = bottomup
    print(subset_sum_count([1, 1, 2, 3], 4))  # 3
    print(subset_sum_count([1, 2, 7, 1, 5], 9))  # 3
    print(subset_sum_count([5, 2, 3, 10, 6, 8], 10))  # 3
    print(subset_sum_count([2, 5, 1, 4, 3], 5))  # 3
    print(subset_sum_count([9, 7, 0, 3, 9, 8, 6, 5, 7, 6], 31))  # 40
