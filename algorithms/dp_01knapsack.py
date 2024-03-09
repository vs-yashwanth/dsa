def recursive(weights, values, capacity):         # O(2**n), O(1)

    def dp(capacity, profit, ind):

        if ind == len(values):
            return profit

        using = 0
        if capacity >= weights[ind]:
            using = dp(capacity-weights[ind], profit + values[ind], ind+1)
        not_using = dp(capacity, profit, ind+1)

        return max(using, not_using)

    return dp(capacity, 0, 0)


def memoized(weights, values, capacity):     # O(n*W), O(n*W)
    memo = {}

    def dp(capacity, profit, ind):

        if (capacity, ind) in memo:
            return memo[(capacity, ind)]

        if ind == len(values):
            return profit

        using = 0
        if capacity >= weights[ind]:
            using = dp(capacity-weights[ind], profit + values[ind], ind+1)
        not_using = dp(capacity, profit, ind+1)

        memo[(capacity, ind)] = max(using, not_using)
        return max(using, not_using)

    return dp(capacity, 0, 0)


def bottomup(weights, prices, capacity):  # O(n*W), O(n*W)

    dp = [[0 for _ in range(capacity+1)] for _ in range(len(prices))]
    for i in range(len(prices)):
        for c in range(1, capacity+1):
            if i == 0 and weights[i] <= c:
                dp[i][c] = prices[i]
                continue
            if weights[i] > c:
                dp[i][c] = dp[i-1][c]
            else:
                dp[i][c] = max(dp[i-1][c], prices[i] + dp[i-1][c-weights[i]])

    return dp[i][capacity]

if __name__ == '__main__':
    val = [4, 5, 3, 7]
    wt = [2, 3, 1, 4]
    W = 5
    n = len(val)
    print(recursive(wt, val, W))
    print(memoized(wt, val, W))
    print(bottomup(wt, val, W))
