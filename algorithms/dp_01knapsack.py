def recursive(weights, values, capacity):         # O(2**n), O(1)

    def dp(capacity, profit, i):

        if i == len(values):
            return profit

        using = 0
        if capacity >= weights[i]:
            using = dp(capacity-weights[i], profit + values[i], i+1)
        not_using = dp(capacity, profit, i+1)

        return max(using, not_using)

    return dp(capacity, 0, 0)


def memoized(weights, values, capacity):     # O(n*W), O(n*W)

    n = len(values)
    memo = {}

    def dp(capacity, i):

        if capacity <= 0 or i == n:
            return 0

        using = 0
        if capacity >= weights[i]:
            using = values[i] + dp(capacity-weights[i], i+1)
        not_using = dp(capacity, i+1)

        memo[(capacity, i)] = max(using, not_using)
        return max(using, not_using)

    return dp(capacity, 0)


def bottomup(weights, profits, capacity):  # O(n*W), O(n*W)

    dp = [[0 for _ in range(capacity+1)] for _ in range(len(profits))]
    for i in range(len(profits)):
        for c in range(1, capacity+1):
            if i == 0 and weights[i] <= c:
                dp[i][c] = profits[i]
                continue
            if weights[i] > c:
                dp[i][c] = dp[i-1][c]
            else:
                dp[i][c] = max(dp[i-1][c], profits[i] + dp[i-1][c-weights[i]])

    i = n
    w = capacity
    used = []
    for i in range(n-1, -1, -1):
        if dp[i][w] != dp[i - 1][w]:
            used.append(profits[i])
            w -= weights[i]

    return dp[-1][-1], used


def bottomup_optimal(weights, profits, capacity):  # O(nw), O(w)

    n = len(profits)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, -1, -1):
            if w >= weights[i]:
                dp[w] = max(dp[w], profits[i] + dp[w - weights[i]])
    
    return dp[-1]



if __name__ == '__main__':
    val = [4, 5, 3, 7]
    wt = [2, 3, 1, 4]
    W = 5
    n = len(val)
    print(recursive(wt, val, W))
    print(memoized(wt, val, W))
    print(bottomup(wt, val, W))
    print(bottomup_optimal(wt, val, W))
