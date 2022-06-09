# Python 3 prorgam for finding max path in matrix
# To calculate max path in matrix

def findMaxPath(mat):       # O(n*m)

    m,n = len(mat), len(mat[0])
    for i in range(1,m):
        maxi = -1
        for j in range(n):
            if j>0 and j<n-1:
                mat[i][j] += max(mat[i-1][j], mat[i-1][j-1], mat[i-1][j+1])
            elif j>0:
                mat[i][j] += max(mat[i-1][j], mat[i-1][j-1])
            elif j<n-1:
                mat[i][j] += max(mat[i-1][j], mat[i-1][j+1])
            maxi = max(maxi,mat[i][j])
            
    return maxi


mat = ([[ 10, 10, 2, 0, 20, 4 ],
		[ 1, 0, 0, 30, 2, 5 ],
		[ 0, 10, 4, 0, 2, 0 ],
		[ 1, 0, 2, 20, 0, 4 ]])
			
print(findMaxPath(mat))


# 30:38