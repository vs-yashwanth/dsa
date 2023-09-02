# implementing paint.fill() on a screen

def floodfill_rec(screen,x,y,prev,new):
    m,n = len(screen), len(screen[0])

    if not 0<=x<m or not 0<=y<n:
        return 
    if screen[x][y] != prev :
        return
    
    screen[x][y] = new

    floodfill_rec(screen,x+1,y,prev,new)
    floodfill_rec(screen,x-1,y,prev,new)
    floodfill_rec(screen,x,y+1,prev,new)
    floodfill_rec(screen,x,y-1,prev,new)


def floodfill_bfs(screen,x,y,new):
    m,n = len(screen), len(screen[0])
    prev = screen[x][y]
    q = [(x,y)]
    neighbours = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        i,j = q.pop(0)
        if screen[i][j] != prev:
            continue
        else:
            screen[i][j] = new
        
        for u,v in neighbours:
            new_i = i + u
            new_j = j + v
            if 0<=new_i<m and 0<=new_j<n:
                if screen[new_i][new_j] == prev:
                    q.append((new_i, new_j))
    
 

if __name__ == '__main__':

    screen = [[1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 0],
            [1, 0, 0, 1, 1, 0, 1, 1],
            [1, 2, 2, 2, 2, 0, 1, 0],
            [1, 1, 1, 2, 2, 0, 1, 0],
            [1, 1, 1, 2, 2, 2, 2, 0],
            [1, 1, 1, 1, 1, 2, 1, 1],
            [1, 1, 1, 1, 1, 2, 2, 1]]

    x = 4
    y = 4
    newC = 3
    #floodfill_rec(screen, x, y,screen[x][y], newC)
    floodfill_bfs(screen,x,y,newC)
    m,n = len(screen), len(screen[0])

    for i in range(m):
        for j in range(n):
            print(screen[i][j], end = ' ')
        print()


