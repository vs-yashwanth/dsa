
def distinct(s):
    return len(set(s)) == len(s)

def naive(string):    # O(n**3)
    n = len(string)
    res = 0
    for i in range(n):
        for j in range(i,n):
            current = string[i:j+1]
            if distinct(current):
                res = max(res, len(current))
        
    return res

def optimal(string):     # O(n), O(n)
    n = len(string)
    seen = {}
    start = 0
    maxi = 0

    for i in range(n):
        if string[i] in seen:
            start = max(start, seen[string[i]]+1)
        if i-start+1 > maxi:
            maxi = i-start+1
            s = string[start:i+1]

        seen[string[i]] = i
    return maxi, s


s = 'geeksforgeeks'
print(naive(s))
print(optimal(s))