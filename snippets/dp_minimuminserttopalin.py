def recursive(string,l,r):
    if l>r:
        return 
    if l==r:
        return 0
    if l == r-1:
        if string[l] == string[r]:
            return 0
        else:
            return 1
    
    if string[l] == string[r]:
        return recursive(string,l+1,r-1)
    else:
        return 1 + min(recursive(string,l+1,r), recursive(string,l,r-1))


def dynamic(string):
    n = len(string)
    table = [[0 for i in range(n)] for j in range(n)]
    l = r = gap = 0
    for gap in range(1,n):
        l = 0
        for r in range(gap,n):
            if string[l] == string[r]:
                table[l][r] = table[l+1][r-1]
            else:
                table[l][r] = 1 + min(table[l+1][r], table[l][r-1])
            l += 1
    return table[0][n-1]

string = 'geeks'
n = len(string)
print(recursive(string,0,n-1))
print(dynamic(string))
