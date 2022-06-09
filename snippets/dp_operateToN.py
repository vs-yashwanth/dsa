# generate n with either +1 or *2 or *3 
# in min steps

def operate(n):

    dp = [float('inf')]*(n+1)
    dp[1] = 0
    for i in range(2,n+1):
        if i%2 == 0:
            dp[i] = min(dp[i//2]+1, dp[i])
        if i%3 == 0:
            dp[i] = min(1 + dp[i//3], dp[i])
        dp[i] = min(dp[i-1]+1, dp[i])
    return dp[n]

print(operate(15))
                