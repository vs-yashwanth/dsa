def coin_change(target,coins):    # O(mn)
    ways = [0]*(target+1)
    ways[0] = 1
    for c in coins:
        for t in range(c,target+1):
            ways[t] += ways[t-c]
    return ways[target]


arr = [1, 2, 3]
m = len(arr)
n = 4
x = coin_change(n, arr)
print (x)