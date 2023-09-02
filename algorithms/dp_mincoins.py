def min_coins(n, denoms):
    ways = [float('inf')]*(n+1)
    ways[0]=0
    for d in denoms:
        for i in range(d,n+1):
            if d<=n:
                ways[i] = min(ways[i], 1+ways[i-d])
    return ways[n]

if __name__ == "__main__":
 
    coins = [9, 6, 5, 1]
    m = len(coins)
    V = 11
    print(min_coins(V,coins))