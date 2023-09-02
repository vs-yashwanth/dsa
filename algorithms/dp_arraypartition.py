# partition such that their diff of sum is small

def naive(A,run,total,i):       # O(2**n)
    if i==0:
        return abs(total-run-run)
    return min(naive(A,run+A[i],total,i-1), naive(A,run,total,i-1))

def bottomup(a):        # O(s*n)
    n = len(a)

    su = sum(a)

    dp = [[0 for i in range(su + 1)]
          for j in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True
  
    for j in range(1, su + 1):
        dp[0][j] = False
  

    for i in range(1, n + 1):
        for j in range(1, su + 1):
  
            # If i'th element is excluded
            dp[i][j] = dp[i - 1][j]
  
            # If i'th element is included
            if a[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - a[i - 1]]

    for j in range(su // 2, -1, -1):
        if dp[n][j] == True:
            diff = su - (2 * j)
            break
  
    return diff

if __name__ == "__main__":
  
    arr = [3, 1, 4, 2, 2, 1]
    n = len(arr)
    print(naive(arr,0,sum(arr),n-1))
    print(bottomup(arr))