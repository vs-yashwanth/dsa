

def bottomup(nums, target):  # O(n * target), O(target)
    
    dp = [False] * (target+1)
    dp[0] = True

    for num in nums:
        for t in range(target, 0, -1):
            if num <= target:
                dp[t] = dp[t] or dp[t - num]
    
    return dp[target]

if __name__ == '__main__':

    subsetsum = bottomup
    print(subsetsum([1, 2, 3, 7], 6))
    print(subsetsum([1, 2, 7, 1, 5], 10))
    print(subsetsum([1, 3, 4, 8], 6))
