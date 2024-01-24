# Dungeon problem with BFS
from queue_py import QueueRaw


def grid_shortest_path(maze):
    steps = 0
    prev = {}
    visited = set()
    rQ = QueueRaw()
    cQ = QueueRaw()
    sr, sc = 0, 0
    current_level = 1
    next_level = 0
    rQ.enqueue(sr)
    cQ.enqueue(sc)

    while not rQ.is_empty():
        r, c = rQ.dequeue(), cQ.dequeue()
        visited.add((r, c))
        if maze[r][c] == 'E':
            return steps, get_path(r, c, prev)
        if maze[r][c] == '#':
            continue
        next_level = explore_neighbours(
            r, c, prev, visited, rQ, cQ, next_level, maze)
        current_level -= 1
        if current_level == 0:
            current_level = next_level
            next_level = 0
            steps += 1
    return -1


def explore_neighbours(r, c, prev, visited, rQ, cQ, next_level, maze):
    visited.add((r, c))
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for i in range(4):
        rn = r + dr[i]
        cn = c + dc[i]
        if (rn < 0 or rn == len(maze)) or (cn < 0 or cn == len(maze[0])) or maze[rn][cn] == '#' or (rn, cn) in visited:
            continue
        rQ.enqueue(rn)
        cQ.enqueue(cn)
        next_level += 1
        prev[(rn, cn)] = (r, c)
    return next_level


def get_path(r, c, prev):
    out = []
    out.append((r, c))
    while (r, c) in prev:
        out.append(prev[(r, c)])
        r, c = prev[(r, c)]
    return out[::-1]


if __name__ == '__main__':
    M = [['S', '.', '.', '#', '.', '.', '.'],
         ['.', '#', '.', '.', '#', '.', '.'],
         ['.', '#', '.', '.', '.', '.', '.'],
         ['.', '.', '#', '#', '.', '.', '.'],
         ['#', '.', '#', 'E', '.', '#', '.']]
    print(grid_shortest_path(M)
          )
