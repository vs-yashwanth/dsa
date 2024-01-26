# shortest distance between 2 nodes
from graph import Graph
from helpers import QueueWithArray

# For unweighted graphs or graphs with equal weights
# use Dijkstra for weighted graphs

# because bfs tries to reach end node with least number of edges possible
# while this works in unweighted graphs, in weighted graphs going through
# multiple edges that have smaller weights is better than a single edge with
# a massive weight.
#

# O(V+E)


def shortest_distance(graph, n1, n2):
    visited = set()
    distance = 0
    queue = QueueWithArray()
    queue.enqueue(n1)
    aux = []
    while not queue.is_empty():
        node = queue.dequeue()
        if node == n2:
            return distance
        visited.add(node)
        for neigh in graph.G[node]:
            if neigh not in visited:
                aux.append(neigh)
        if queue.is_empty():
            distance += 1
            for i in aux:
                queue.enqueue(i)
            aux.clear()
    return -1


def shortest_path(graph, n1, n2):
    path = [n2]
    prev = {}
    bfs(graph, n1, n2, prev)
    cur = n2
    while cur in prev:
        path.append(prev[cur])
        cur = prev[cur]
    return path[::-1]


def bfs(graph, n1, n2, prev):
    visited = set()
    queue = QueueWithArray()
    queue.enqueue(n1)
    while not queue.is_empty():
        node = queue.dequeue()
        visited.add(node)
        if node == n2:
            return
        for neigh in graph.G[node]:
            if neigh not in visited:
                prev[neigh] = node
                queue.enqueue(neigh)


if __name__ == '__main__':

    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(1, 4)
    graph.add_edge(4, 5)

    print('dist: ', shortest_distance(graph, 0, 5))
    print(shortest_path(graph, 0, 5))

    # graph.visualize()


# -------- useful links --------------

# https://www.baeldung.com/cs/graph-algorithms-bfs-dijkstra
# https://visualgo.net/en/sssp/print#:~:text=The%20O(V%2BE)%20Breadth%2D,edge%20weights%20of%20the%20example
