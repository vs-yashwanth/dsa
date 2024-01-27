from graph import Graph

# strongly connected components - all the nodes can reach all other nodes
# SCCs will have the same low_link values, but low_links values differ based on
# where the dfs is started. So we maintain a stack that tracks the current component
# nodes and groups them into a scc during the dfs callbacks.
#
# O(V+E)


def scc_tarzan(G):
    graph = G.G
    nodes = G.nodes
    stack = []
    on_stack = [False]*len(nodes)
    time = 0
    times = [-1]*len(nodes)
    low_links = [-1]*len(nodes)
    sccs = []
    visited = set()

    for u in nodes:
        if u not in visited:
            time = dfs(u, graph, nodes, stack, time,
                       times, low_links, sccs, visited, on_stack)
    return sccs


def dfs(u, graph, nodes, stack, time, times, low_links, sccs, visited, on_stack):
    visited.add(u)
    stack.append(u)
    on_stack[u] = True
    times[u] = low_links[u] = time
    time += 1

    for v in graph[u]:
        if v not in visited:
            time = dfs(v, graph, nodes, stack, time,
                       times, low_links, sccs, visited, on_stack)
        if on_stack[v]:
            low_links[u] = min(low_links[u], low_links[v])

    if times[u] == low_links[u]:
        cur_component = []
        cur = None
        while cur != u:
            cur = stack.pop()
            on_stack[cur] = False
            cur_component.append(cur)
            low_links[cur] = times[u]
        sccs.append(cur_component)

    return time


if __name__ == '__main__':

    g1 = Graph()
    g1.add_edge(1, 0)
    g1.add_edge(0, 2)
    g1.add_edge(2, 1)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)

    print(scc_tarzan(g1))
    # g1.visualize()

    g2 = Graph()
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    print(scc_tarzan(g2))
    # g2.visualize()

    g3 = Graph()
    g3.add_edge(0, 1)
    g3.add_edge(1, 2)
    g3.add_edge(2, 0)
    g3.add_edge(1, 3)
    g3.add_edge(1, 4)
    g3.add_edge(1, 6)
    g3.add_edge(3, 5)
    g3.add_edge(4, 5)
    print(scc_tarzan(g3))
    # g3.visualize()

    g4 = Graph()
    g4.add_edge(0, 1)
    g4.add_edge(0, 3)
    g4.add_edge(1, 2)
    g4.add_edge(1, 4)
    g4.add_edge(2, 0)
    g4.add_edge(2, 6)
    g4.add_edge(3, 2)
    g4.add_edge(4, 5)
    g4.add_edge(4, 6)
    g4.add_edge(5, 6)
    g4.add_edge(5, 7)
    g4.add_edge(5, 8)
    g4.add_edge(5, 9)
    g4.add_edge(6, 4)
    g4.add_edge(7, 9)
    g4.add_edge(8, 9)
    g4.add_edge(9, 8)
    print(scc_tarzan(g4))
    # g4.visualize()

    g5 = Graph()
    g5.add_edge(0, 1)
    g5.add_edge(1, 2)
    g5.add_edge(2, 3)
    g5.add_edge(2, 4)
    g5.add_edge(3, 0)
    print(scc_tarzan(g5))
    # g5.visualize()
