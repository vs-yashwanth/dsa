
def lcsubstr(s1,s2):
    m,n = len(s1), len(s2)
    table = [[0 for i in range(n)] for j in range(m)]
    out = 0
    out_str = ''

        
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                table[i][j] = 1+table[i-1][j-1]
                if out < table[i][j]:
                    out = table[i][j]
                    row = i
                    col = j    
            else:
                table[i][j] = 0

    while table[row][col] != 0:
        out_str += s1[row]
        row -= 1
        col -= 1
    return out, out_str[::-1]


X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'


m = len(X)
n = len(Y)
 
print(lcsubstr(X,Y))