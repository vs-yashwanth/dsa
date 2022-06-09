def rotten(array):
    m = len(array)
    n = len(array[0])
    q = []
    for i in range(m):
        for j in range(n):
            if array[i][j] == 2:
                q.append((i,j))
    new_q = []
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    time = 0
    while q:
        x,y = q.pop(0)

        for k in range(4):
            i = dr[k]
            j = dc[k]

            r = x+i
            c = y+j
            if 0<=r<m and 0<=c<n:
                if array[r][c] == 1:
                    array[r][c] = 2
                    new_q.append((r,c))
        
        if not q:
            if not new_q:
                break        
            time += 1
            q[:] = new_q.copy()
            new_q = []


    for i in range(m):
        for j in range(n):
            if array[i][j] == 1:
                time = -1
                break
    
    return time


if __name__ == '__main__':
    arr = [[2, 1, 0, 2, 1],
         [1, 0, 1, 2, 1],
         [1, 0, 0, 2, 1]]
    ans = rotten(arr)
    print(ans)