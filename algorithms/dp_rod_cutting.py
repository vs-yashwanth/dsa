# cut a rod into pieces that combined gives the maxmimum profit

def topdown(prices, n):  # O(n**2), O(n)

    memo = {}
    def recurse(n):

        if n < 0:
            return -float('inf')
        elif n == 0:
            return 0

        if n in memo:
            return memo[n]

        max_here = 0
        for i in range(1, n + 1):
            max_here = max(max_here, prices[i] + recurse(n - i))

        memo[n] = max_here
        return max_here

    return recurse(n)

def bottomup(prices, n):  # O(n**2), O(n)

    dp = [0] * (n + 1)

    for l in range(1, n + 1):
        max_here = 0
        for i in range(1, l + 1):
            max_here = max(max_here, prices[i] + dp[l - i])

        dp[l] = max_here

    return dp[-1]

def solution(prices, n): 
    # actual lengths the rod is cut into
    decisions = [-1] * (n + 1)
    dp = [0] * (n + 1)

    for l in range(1, n + 1):
        max_here = 0
        cut = -1
        for i in range(1, l + 1):
            profit = prices[i] + dp[l - i]
            if profit > max_here:
                max_here = profit
                cut = i
        
        dp[l] = max_here 
        decisions[l] = cut
    
    cuts = []
    while n > 0:
        cuts.append(decisions[n])
        n -= decisions[n]

    return dp[-1], cuts


if __name__ == '__main__':

    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 7

    print(topdown(prices, n))
    print(bottomup(prices, n))
    print(solution(prices, n))
