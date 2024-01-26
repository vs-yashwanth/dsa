from graph import Graph
import heapq as pq

# single source shortest path, shortest path between two nodes
# no negative weights

# O(E log(V))
# optimizations can be done using indexed priortiy queues, d-ary heaps, fibonacci heaps
# which gives a complexity of O(E + V log(V))


def sssp_dijkstra(G, start):
    graph = G.G
    n = len(G.nodes)
    dist = [float('inf')]*n
    dist[start] = 0
    prev = {}
    priority_queue = []
    visited = set()

    pq.heappush(priority_queue, (0, start))
    while priority_queue:
        d, u = pq.heappop(priority_queue)
        visited.add(u)

        for v, w in graph[u]:
            if v not in visited:
                if d+w < dist[v]:
                    dist[v] = d+w
                    pq.heappush(priority_queue, (d+w, v))
                    prev[v] = u
    return dist, prev


def get_shortest_path(G, start, end):
    dist, prev = sssp_dijkstra(G, start)
    dist = dist[end]
    out = [end]
    while end in prev:
        out.append(prev[end])
        end = prev[end]
    return out[::-1], dist


if __name__ == '__main__':

    graph = Graph(weighted=True)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)

    print(sssp_dijkstra(graph, 0)[0])
    print(get_shortest_path(graph, 0, 5))
