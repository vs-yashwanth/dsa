def main():
    #grid = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
    grid = [[0, 0, 1, 1], [0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    m = len(grid)
    n = len(grid[0])
    d1 = [1, 0, -1, 0, 1, -1, -1, 1]
    d2 = [0, 1, 0, -1, 1, 1, -1, -1]
    dirs = list(zip(d1,d2))
    global visited
    global size
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and (i,j) not in visited:
                size = 0
                count(grid,i,j,dirs)
    
    return largest

def count(grid,i,j,dirs):
    global largest
    global visited
    global size

    m = len(grid)
    n = len(grid[0])

    visited.add((i,j))
    size += 1
    if size>largest:
        largest = size
    #print(i,j,largest,size)
    #print(visited)
    for p,q in dirs:
        new_i = i + p
        new_j = j + q
        if (0<=new_i<m and 0<=new_j<n) and grid[new_i][new_j] == 1 and (new_i,new_j) not in visited:
            count(grid,new_i,new_j,dirs)

largest = 0
visited = set()
size = 0

print(main())

