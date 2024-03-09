
def bruteforce(nums):  # O(2**n), O(n)
    total = sum(nums)

    def backtrack(cur_sum, i):
        if i == len(nums):
            return abs(cur_sum - (total - cur_sum))

        not_using = backtrack(cur_sum, i+1)
        using = cur_sum
        if cur_sum + nums[i] < total:
            using = backtrack(cur_sum + nums[i], i+1)

        return min(using, not_using)

    return backtrack(0, 0)


def topdown(nums):  # O(n * sum), O(n * sum)
    memo = {}
    total = sum(nums)

    def dp(cur_sum, i):

        if i == len(nums):
            return abs(cur_sum - (total - cur_sum))

        if (i, cur_sum) in memo:
            return memo[(i, cur_sum)]

        not_using = dp(cur_sum, i+1)
        using = cur_sum
        if cur_sum + nums[i] < total:
            using = dp(cur_sum + nums[i], i+1)

        memo[(i, cur_sum)] = min(using, not_using)
        return memo[(i, cur_sum)]

    return dp(0, 0)

# for each num add it to the first or sec set and get the min achieved


def topdown2(nums):   # O(n * sum), O(n * sum)
    memo = {}
    total = sum(nums)

    def dp(s1, s2, i):
        if i == len(nums):
            return abs(s1 - s2)
        if (s1, s2) in memo:
            return memo[(s1, s2)]

        opt1 = float('inf')
        if s1 + nums[i] < total:
            opt1 = dp(s1 + nums[i], s2, i+1)

        opt2 = float('inf')
        if s1 + nums[i] < total:
            opt2 = dp(s1, s2 + nums[i], i+1)

        memo[(s1, s2)] = min(opt1, opt2)
        return memo[(s1, s2)]

    return dp(0, 0, 0)


def bottomup(nums):  # O(n * sum), O(n)

    total = sum(nums)
    dp = [False for _ in range(total+1)]
    dp[0] = True

    for num in nums:
        for t in range(total//2, 0, -1):
            if num <= t:
                dp[t] = dp[t] or dp[t-num]

    i = total
    while i >= 0:
        if dp[i]:
            break
        i -= 1
    return abs(i - (total - i))


if __name__ == '__main__':

    min_subset_sum_diff = bottomup

    print(min_subset_sum_diff([1, 2, 3, 9]))  # 3
    print(min_subset_sum_diff([1, 2, 7, 1, 5]))   # 0
    print(min_subset_sum_diff([1, 3, 100, 4]))  # 92
