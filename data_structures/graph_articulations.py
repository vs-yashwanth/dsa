from graph import Graph

# articulation points are those whose removal increases the no of connected
# components in the graph. they can be at the beginning of a cycle, one of the
# two nodes on a bridge but the root of dfs must have atleast 2 outgoing edges.
#
# for undirected graphs

# O(V+E)


def articulations(G):
    graph = G.G
    nodes = G.nodes
    articulations = set()
    time = 0
    times = [0]*len(nodes)
    low_links = [0]*len(nodes)
    root_out_edges = 0
    visited = set()

    for u in nodes:
        if u not in visited:
            root_out_edges = 0
            root_out_edges, time = dfs(
                u, u, -1, graph, nodes, articulations, time, times, low_links, root_out_edges, visited)
            if root_out_edges > 1:
                articulations.add(u)
            else:
                articulations.remove(u)

    return articulations


def dfs(root, u, parent, graph, nodes, articulations, time, times, low_links, root_out_edges, visited):
    visited.add(u)
    times[u] = low_links[u] = time
    time += 1
    if root == parent:
        root_out_edges += 1
    for v in graph[u]:
        if v == parent:
            continue
        if v not in visited:
            root_out_edges, time = dfs(
                root, v, u, graph, nodes, articulations, time, times, low_links, root_out_edges, visited)
            low_links[u] = min(low_links[u], low_links[v])
            if times[u] <= low_links[v]:
                articulations.add(u)
        else:
            low_links[u] = min(low_links[u], times[v])

    return root_out_edges, time


if __name__ == '__main__':

    g1 = Graph()
    g1.add_edge(1, 0)
    g1.add_edge(0, 2)
    g1.add_edge(2, 1)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)
    print(articulations(g1))
    # g1.visualize()

    g2 = Graph()
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    print(articulations(g2))
    # g2.visualize()

    g3 = Graph(directed=False)
    g3.add_edge(0, 1)
    g3.add_edge(1, 2)
    g3.add_edge(2, 0)
    g3.add_edge(1, 3)
    g3.add_edge(1, 4)
    g3.add_edge(1, 6)
    g3.add_edge(3, 5)
    g3.add_edge(4, 5)
    print(articulations(g3))
    # g3.visualize()
    # 3 was an articulation point when the graph is directed


# In a directed graph, the concept of "articulation points" is not applicable
# directly. Instead, we use the concept of strongly connected components (SCCs)
# to find nodes that, when removed, increase the number of SCCs.
