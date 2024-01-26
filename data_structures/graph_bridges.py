from graph import Graph

# bridges are edges whose removal increases the number of connected
# components. We maintain discovery times of each node while dfs and
# and whenever the least timed node reachable by the next node (low_link)
# is greater than the current node's time, then that edge is a bridge
# this means that the next node cannot reach the prev nodes and is a
# seperate component

# O(V+E)


def bridges(G):
    graph = G.G
    nodes = G.nodes
    bridges = []
    n = len(nodes)
    time = 0
    times = [0]*n
    low_links = [0]*n
    visited = set()

    for u in nodes:
        if u not in visited:
            time = dfs(u, -1, time, times, low_links, visited, graph, bridges)

    return bridges


def dfs(u, parent, time, times, low_links, visited, graph, bridges):
    visited.add(u)
    times[time] = low_links[time] = time
    time += 1
    for v in graph[u]:
        if v == parent:
            continue
        if v in visited:
            low_links[u] = min(low_links[u], times[v])
        else:
            time = dfs(v, u, time, times, low_links, visited, graph, bridges)
            low_links[u] = min(low_links[u], low_links[v])
            if times[u] < low_links[v]:
                bridges.append((u, v))
    return time


if __name__ == '__main__':

    g1 = Graph(directed=False)
    g1.add_edge(1, 0)
    g1.add_edge(0, 2)
    g1.add_edge(2, 1)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)
    print(bridges(g1))  # (3,4) , (0,3)

    g2 = Graph(directed=False)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    print(bridges(g2))  # [(2, 3), (1, 2), (0, 1)]

    g3 = Graph(directed=False)
    g3.add_edge(0, 1)
    g3.add_edge(1, 2)
    g3.add_edge(2, 0)
    g3.add_edge(1, 3)
    g3.add_edge(1, 4)
    g3.add_edge(1, 6)
    g3.add_edge(3, 5)
    g3.add_edge(4, 5)
    print(bridges(g3))  # [(1,6)]
    # g3.visualize()
