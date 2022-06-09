def recursive(weights,values,W,n):         # O(2**n), O(1)
    if n == 0 or W==0:
        return 0
    
    if weights[n-1] > W:
        return recursive(weights, values, W,n-1)

    return max(values[n-1] + recursive(weights,values,W-weights[n-1],n-1) , 
                recursive(weights, values, W,n-1))

def memoized(weights,values,W,n,memo = {}):     # O(n*W), O(n*W)
    key = f'{W},{n}'
    if key in memo:
        return memo[key]
    if n==0 or W==0:
        return 0
    if weights[n-1] > W:
        memo[key] = memoized(weights,values,W,n-1,memo)
        return memo[key]
    memo[key] = max(values[n-1]+memoized(weights,values,W-weights[n-1],n-1),
                    memoized(weights, values, W, n-1))
    return memo[key]
    
def bottomup(weights,values,W,n):
    table = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            if weights[i-1] <= j:
                table[i][j] = max(values[i-1] + table[i-1][j-weights[i-1]],
                                table[i-1][j])
            else:
                table[i][j] = table[i-1][j]
    return table[n][W]

if __name__ == '__main__':
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(recursive( wt, val,W, n))
    print(memoized( wt, val,W, n))
    print(bottomup( wt, val,W, n))