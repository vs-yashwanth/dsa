def counter(n):
    if n<=1:
        return 1
    sum = 0
    for root in range(1,n+1):
        left = counter(root-1)
        right = counter(n-root)
        sum += left*right
    return sum


print(counter(3))