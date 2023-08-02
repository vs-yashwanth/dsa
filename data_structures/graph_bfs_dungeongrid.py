# Dungeon problem with BFS

        
M = [['S', '.', '.', '#', '.', '.', '.'],
     ['.', '#', '.', '.', '#', '.', '.'],
     ['.', '#', '.', '.', '.', '.', '.'],
     ['.', '.', '#', '#', '.', '.', '.'],
     ['#', '.', '#', 'E', '.', '#', '.']]

R,C = len(M), len(M[0])
sr = sc = 0
rq = []
cq = []
path = []

visited = [[False for i in range(C)] for j in range(R)]
nodes_now = 1
nodes_next = 0
steps = 0

reached_end = False

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def solve():
    global nodes_now, nodes_next, steps, reached_end
    
    visited[sr][sc] = True
    rq.append(sr)
    cq.append(sc)
    
    while rq:
        r = rq.pop(0)
        c = cq.pop(0)
        if M[r][c] == 'E':
            reached_end = True
            break
        neighbours(r,c)
        nodes_now -= 1
        if nodes_now == 0:
            nodes_now = nodes_next
            nodes_next = 0
            steps += 1
            path.append((r,c))
    if reached_end:
        return steps
    return -1

def neighbours(r,c):
    global nodes_next
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        
        if rr>=R or cc>=C:
            continue
        if rr<0 or cc<0:
            continue
        if M[rr][cc] == '#':
            continue
        if visited[rr][cc] == True:
            continue
        rq.append(rr)
        cq.append(cc)
        visited[r][c] = True

        nodes_next += 1
        
print(solve())
#print(path)
#print(visited)
