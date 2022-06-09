def count_triplets(arr):
    """sum of two is equal to third"""
    n = len(arr)
    maxi = max(arr)
    freq = [0 for i in range(maxi+1)]
    for e in arr:
        freq[e] += 1
    
    res = 0

    # 0 + 0 = 0
    res += freq[0]*(freq[0]-1)*(freq[0]-2)//6

    # 0 + x = x
    for i in range(1,maxi+1):
        res += freq[0] * freq[i] * (freq[i] - 1) // 2
    
    # x + x = 2x
    for i in range(1,(maxi+1)//2):
        res += freq[i]*(freq[i]-1)*freq[i*2] // 2
    
    # x + y = z
    for i in range(1,maxi+1):
        for j in range(i+1,maxi+1-i):
            res +=  freq[i]*freq[j]*freq[i+j]
    
    return res

print(count_triplets([1,2,3,4,5]))
