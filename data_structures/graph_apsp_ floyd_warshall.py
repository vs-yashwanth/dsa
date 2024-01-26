# shortest paths between all pairs of nodes
# can work with negative weights
# good for dense graphs with < 200 nodes
# works with adjacency matrix representation


# O(V**3)

def apsp_floyd_warshall(graph):
    n = len(graph)
    dp = [[j for j in i] for i in graph]
    nxt = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] != float('inf'):
                nxt[i][j] = j

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    nxt[i][j] = nxt[i][k]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = -float('inf')
                    nxt[i][j] = -1
    return dp, nxt


def get_shortest_paths(start, end, dp, nxt):
    if dp[start][end] == float('inf'):
        return []
    out = [start]
    cur = start
    while cur != end:
        cur = nxt[cur][end]
        if cur == -1:
            return None
        out.append(cur)

    return out, dp[start][end]


if __name__ == "__main__":

    graph = [[0, 5, float('inf'), 10],
             [float('inf'), 0, 3, float('inf')],
             [float('inf'), float('inf'), 0, 1],
             [float('inf'), float('inf'), float('inf'), 0]
             ]

    dp, nxt = apsp_floyd_warshall(graph)
    print(dp)
    print(get_shortest_paths(0, 3, dp, nxt))
