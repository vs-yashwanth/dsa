from graph import Graph


def connected_components(graph):
    visited = set()
    components = []
    current = []
    for node in list(graph.G.keys()):
        if node not in visited:
            current = []
            dfs(graph, node, visited, current)
            components.append(current)
    return components


def dfs(graph, node, visited, current):
    visited.add(node)
    current.append(node)
    for neighbour in graph.G[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, current)


if __name__ == "__main__":

    g = Graph()

    g.addEdge(1, 0)
    g.addEdge(1, 5)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(5, 6)
    g.addEdge(5, 1)

    print(connected_components(g))
    g.visualize()
