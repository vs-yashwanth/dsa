def remove(coins, k):
    mini = min(coins)
    rem = 0
    for i in coins:
        diff = i-mini
        if diff > k:
            rem += diff - k
    return rem

a = [1, 5, 1, 2, 5, 1];
n = len(a);
k = 3;
print(remove(a,  k)); 
