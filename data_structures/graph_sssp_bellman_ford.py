from graph import Graph

# for negative weighted graphs
# O(VE)

# why v-1 iterations?
# the shortest path between two nodes in a graph with total v nodes is
# atmost v-1 edges long. It means it includes all the nodes atmost once.
# bellman ford has a property - after k iterations, we know the minimum paths
# between two nodes with paths restriced to length k edges long. this is because
# in each iteration we use the dists from previous and update if a shorter path is found
# i.e add a new edge to the path that makes the path shorter. so after v-1 iterations
# we will have shortest path that considers/includes all nodes.

# so if we are able to decrease the dist even further after v-1 iterations,
# it means that the path includes more than v nodes and some nodes are repeating
# which ultimately means that there is a negaitve loop


def sssp_bellman_ford(G, start):
    graph = G.G
    num_nodes = len(G.nodes)
    dist = [float('inf')]*num_nodes
    dist[start] = 0
    prev = {}

    for _ in range(num_nodes-1):
        for u in list(graph.keys()):
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u]+w
                    prev[v] = u

    for _ in range(num_nodes-1):
        for u in list(graph.keys()):
            for v, w in graph[u]:
                if dist[u]+w < dist[v]:
                    dist[v] = -float('inf')
                    prev[v] = u

    return dist, prev


def get_shortest_path(G, start, end):
    dist, prev = sssp_bellman_ford(G, start)
    dist = dist[end]
    out = [end]
    while end in prev:
        out.append(prev[end])
        end = prev[end]
    return out[::-1], dist


if __name__ == '__main__':

    g = Graph(weighted=True)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    print(sssp_bellman_ford(g, 0)[0])
    print(get_shortest_path(g, 0, 2))


# --- useful links --------

# https://stackoverflow.com/questions/48138952/bellman-ford-why-are-there-n-1-iterations-for-calculating-mindistance
# https://cs.stackexchange.com/questions/50557/why-do-we-need-to-run-the-bellman-ford-algorithm-for-n-1-times#:~:text=As%20to%20your%20second%20question,you%20need%20n%E2%88%921%20iterations.
