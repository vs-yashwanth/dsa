from collections import defaultdict

    
def floyd_warshall(graph):
    n = len(graph)
    visited = {}
    memo = [[0 for i in range(n)] for j in range(n)]
    
    next = [[None for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            memo[i][j] = graph[i][j]
            if graph[i][j] != float('inf'):
                next[i][j] = j

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if memo[i][k] + memo[k][j] < memo[i][j]:
                    memo[i][j] = memo[i][k] + memo[k][j]
                    next[i][j] = next[i][k]
    
    # check negative cycles

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if memo[i][j] > memo[i][k]+memo[k][j]:
                    memo[i][j] = -float('inf')
                    next[i][j] = -1
    
    return memo, next


def build(start, end, memo, next):
    path = []
    if memo[start][end] == float('inf'):
        return path
    while start != end:
        start = next[start][end]
        if start == -1:
            return None
        path.append(start)
    
    if next[start][end] == -1:
        return None
    path.append(end)
    return path

INF = float('inf')
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]
memo, next = floyd_warshall(graph)
print(memo)




