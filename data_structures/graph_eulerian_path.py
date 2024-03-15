from graph import Graph

# Eulerian path - path of edges that goes through each edge exacly once
# Eulerian cycle - path of edges that goes through all edges and returns to starting edge

# this code is for directed graphs

# O(E)


def eulerian_path_directed(G):
    graph = {key: []+value for key, value in G.G.items()}
    nodes = G.nodes
    path = []
    in_edges = [0]*len(nodes)
    out_edges = [0]*len(nodes)
    num_edges = 0
    path_exists, in_edges, out_edges, num_edges = check_eulerian_path(
        graph, in_edges, out_edges, num_edges)
    if not path_exists:
        return path
    start_node = get_start_node(in_edges, out_edges, len(nodes))

    dfs(start_node, graph, path, out_edges)
    if len(path) != num_edges+1:
        return None, path[::-1]
    else:
        return path[::-1]


def dfs(u, graph, path, out_edges):

    while out_edges[u]:
        out_edges[u] -= 1
        nxt = graph[u].pop()
        dfs(nxt, graph, path, out_edges)

    path.append(u)


def check_eulerian_path(graph, in_edges, out_edges, num_edges):
    for u in list(graph.keys()):
        for v in graph[u]:
            out_edges[u] += 1
            in_edges[v] += 1
            num_edges += 1

    start = end = 0
    for i in range(len(in_edges)):
        if in_edges[i] - out_edges[i] > 1 or out_edges[i] - in_edges[i] > 1:
            return False, in_edges, out_edges, num_edges
        elif out_edges[i] - in_edges[i] == 1:
            start += 1
        elif in_edges[i] - out_edges[i] == 1:
            end += 1

    path_exists = bool((start == 0 and end == 0) or (start == 1 and end == 1))

    return path_exists, in_edges, out_edges, num_edges


def get_start_node(in_edges, out_edges, n):
    start_node = None
    for i in range(n):
        if out_edges[i] - in_edges[i] == 1:
            return i
        if out_edges[i] > 0:
            start_node = i
    return start_node


if __name__ == '__main__':

    g1 = Graph()
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 0)
    g1.add_edge(1, 3)
    g1.add_edge(3, 4)
    g1.add_edge(4, 1)
    print(eulerian_path_directed(g1))
    # g1.visualize()
    # Expected Output: Eulerian Path: [4, 1, 2, 0, 1, 3, 4]

    g2 = Graph()
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(3, 0)
    g2.add_edge(3, 1)
    print(eulerian_path_directed(g2))
    # g2.visualize()
    # Expected Output: Eulerian Path: [3, 1, 2, 3, 0, 1]

    g3 = Graph()
    g3.add_edge(0, 1)
    g3.add_edge(1, 2)
    g3.add_edge(2, 3)
    g3.add_edge(3, 0)
    g3.add_edge(0, 2)
    print(eulerian_path_directed(g3))
    # Expected Output: [0, 2, 3, 0, 1, 2]
    # g3.visualize()

    g4 = Graph()
    g4.add_edge(0, 1)
    g4.add_edge(1, 2)
    g4.add_edge(2, 3)
    g4.add_edge(3, 0)
    g4.add_edge(2, 4)
    g4.add_edge(4, 2)
    print(eulerian_path_directed(g4))
    # Expected Output: [4, 2, 3, 0, 1, 2, 4]
    # g4.visualize()

    g5 = Graph()
    g5.add_edge(0, 1)
    g5.add_edge(1, 2)
    g5.add_edge(2, 3)
    g5.add_edge(3, 0)
    g5.add_edge(0, 2)
    g5.add_edge(2, 1)
    g5.add_edge(1, 3)
    print(eulerian_path_directed(g5))
    # g5.visualize()
    # Expected Output: Eulerian Path: [0, 2, 1, 3, 0, 1, 2, 3]

    g6 = Graph()
    g6.add_edge(0, 1)
    g6.add_edge(0, 2)
    g6.add_edge(2, 0)
    print(eulerian_path_directed(g6))
    # Expected Output: [0, 2, 0, 1]


# useful links
# https://www.topcoder.com/thrive/articles/eulerian-path-and-circuit-in-graphs
