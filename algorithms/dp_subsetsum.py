def bruteforce(nums, target):  # O(2**n), O(n)

    def backtrack(ind, target):
        if target == 0:
            return True
        if ind == len(nums) or target < 0:
            return False

        return backtrack(ind+1, target) or backtrack(ind+1, target-nums[ind])

    return backtrack(0, target)


def topdown(nums, target):  # O(n * target), O(n * target)
    memo = {}

    def dp(ind, target):
        if target == 0:
            return True
        if ind == len(nums) or target < 0:
            return False
        if (ind, target) in memo:
            return memo[(ind, target)]

        memo[(ind, target)] = dp(
            ind+1, target) or dp(ind+1, target-nums[ind])
        return memo[(ind, target)]

    return dp(0, target)


def bottomup(nums, target):  # O(n * target), O(target)

    dp = [False] * (target+1)
    dp[0] = True

    for num in nums:
        for t in range(target, 0, -1):
            if num <= target:
                dp[t] = dp[t] or dp[t - num]

    return dp[target]


if __name__ == '__main__':

    subsetsum = topdown
    print(subsetsum([1, 2, 3, 7], 6))
    print(subsetsum([1, 2, 7, 1, 5], 10))
    print(subsetsum([1, 3, 4, 8], 6))
