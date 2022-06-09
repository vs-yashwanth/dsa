def main():
    a = [0,2,1,2,2,3]
    print(find(a))
    print(find2(a))

def find(a):   #O(n^2)
    for i in range(len(a)):
        if a[i] in a[i+1:]:
            return a[i]
    return None

def find2(a):
    s = {}
    n = len(a)
    for i in range(n):
        if a[i] not in s:
            s[a[i]] = i
        elif a[i] in s and s[a[i]] > 0:
            s[a[i]] *= -1
        elif a[i] in s and s[a[i]] == 0:
            s[a[i]] = None
        else:
            pass
    maxi = -100000
    out = None
    for i in s:
        if s[i] == None:
            return i
        if s[i] < 0:
            if s[i] >  maxi:
                maxi = s[i]
                out = i
    return out

main()