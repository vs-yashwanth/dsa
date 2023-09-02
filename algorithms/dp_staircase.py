def naive(n):       # O(3**n)
    if n<0:
        return 0
    if n==0:
        return 1
    return naive(n-1)+naive(n-2)+naive(n-3)

def bottomup(n):        # O(n), O(n)
    table = [0]*(n+1)
    table[0] = 1
    if n>=2:
        table[1] = 1
        table[2] = 2
    for i in range(3,n+1):
        table[i] = table[i-1]+table[i-2]+table[i-3]
    return table[n]

def optimal(n):         # O(n), O(1)
    table = [0]*3
    table[0] = table[1] = 1
    table[2] = 2
    for i in range(3,n+1):
        table[i%3] = table[(i-1)%3] + table[(i-2)%3] + table[(i-3)%3]
    return table[n%3]


print(naive(4))
print(bottomup(4))
print(optimal(4))