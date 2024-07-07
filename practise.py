def findMaxForm( strs, m, n) -> int:

    len_strs = len(strs)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    print(dp)

    for i in range(len_strs):
        for j in range(m, -1, -1):
            for k in range(n, -1, -1):
                count0 = strs[i].count('0')
                count1 = strs[i].count('1')
                print(count0, count1)

                if j >= count0 and k >= count1:
                    print(len(dp)j, k, j - count0, k - count1)

                    dp[j][k] = max(
                        dp[j][k], 1 + dp[j - count0][k - count1])

    return dp[-1][-1]


print(findMaxForm(["10", "0001","111001","1","0"], 5, 3))