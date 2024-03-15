# where some events might occur before others
# cyclic graphs cannot be topologically sorted

from collections import deque
from collections import defaultdict
from graph import Graph

# https://leetcode.com/problems/course-schedule-ii/submissions/1196043806/


def topological_sort(g, weighted=False):
    graph = g.G
    visited = set()
    visiting = set()
    order = []

    def dfs(u):
        visited.add(u)
        visiting.add(u)
    
        for v in graph[u]:
            if weighted:
                v, w = v
            if v not in visited:
                if dfs(v):
                    return True
            elif v in visiting:
                return True

        visiting.discard(u)
        order.append(u)

    for u in list(graph.keys()):
        if u not in visited:
            if dfs(u):
                return -1

    return order[::-1]


def khans_algo(G):  # O(v+e), O(v)
    graph = G.G
    indegrees = defaultdict(int)
    queue = deque()
    out = []

    for u in list(graph.keys()):
        for v in graph[u]:
            indegrees[v] += 1

    for node in G.nodes:
        if indegrees[node] == 0:
            queue.append(node)

    while queue:
        cur = queue.popleft()
        out.append(cur)
        for v in graph[cur]:
            indegrees[v] -= 1
            if indegrees[v] == 0:
                queue.append(v)

    if len(out) != len(G.nodes):
        return -1

    return out


if __name__ == '__main__':

    G = Graph()
    G.add_edge(0, 1)
    G.add_edge(1, 2)
    G.add_edge(1, 6)
    G.add_edge(1, 7)
    G.add_edge(6, 8)
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(2, 5)

    top = topological_sort

    print(top(G))
    # G.visualize()
