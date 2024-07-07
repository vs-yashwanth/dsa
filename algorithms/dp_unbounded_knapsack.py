# 01 knapsack but can pick each element any number of times


def topdown(profits, weights, limit):  # O(nw), O(w)

    n = len(weights)
    memo = {}

    def recurse(capacity):
        if capacity < 0:
            return -float('inf')

        if capacity == 0:
            return 0

        if capacity in memo:
            return memo[capacity]

        max_here = 0
        for i in range(n):
            max_here = max(
                max_here, profits[i] + recurse(capacity - weights[i]))

        memo[capacity] = max_here
        return max_here

    return recurse(limit)


def topdown2(profits, weights, limit):  # O(nw), O(nw)

    n = len(profits)
    memo = {}

    def recurse(i, capacity):

        if capacity < 0:
            return -float('inf')
        elif capacity == 0:
            return 0

        if i == n:
            return -float('inf')

        if (i, capacity) in memo:
            return memo[(i, capacity)]

        using = 0
        if weights[i] <= capacity:
            using = profits[i] + recurse(i, capacity - weights[i])

        not_using = recurse(i + 1, capacity)

        memo[(i, capacity)] = max(using, not_using)
        return memo[(i, capacity)]

    return recurse(0, limit)


def bottomup(profits, weights, limit):  # O(nw), O(w)

    n = len(profits)
    dp = [0] * (limit + 1)

    for l in range(limit + 1):
        max_here = 0
        for i in range(n):
            if weights[i] <= l:
                max_here = max(max_here, profits[i] + dp[l - weights[i]])
        dp[l] = max_here

    return dp[-1]


if __name__ == '__main__':

    profits = [6, 1, 7, 7]
    weights = [1, 3, 4, 5]
    limit = 8

    print(topdown(profits, weights, limit))  # 48
    print(bottomup(profits, weights, limit))  # 48
    print(topdown2(profits, weights, limit))  # 48
