# get all possible topologically sorted orders

from collections import defaultdict, deque
from graph import Graph


def topsort_all(pres, n):  # O(v! * e), O(v! * e)
    graph = Graph()
    indegrees = defaultdict(int)
    for u, v in pres:
        graph.add_edge(u, v)
        indegrees[v] += 1
    all_orders = []
    queue = deque()
    for i in range(n):
        if indegrees[i] == 0:
            queue.append(i)

    def backtrack(queue, order):

        for node in queue:
            next_queue = deque(queue)
            next_queue.remove(node)
            order.append(node)
            if len(order) == n:
                all_orders.append(order[:])

            for v in graph.G[node]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    next_queue.append(v)

            backtrack(next_queue, order)

            order.pop()
            for v in graph.G[node]:
                indegrees[v] += 1

    backtrack(queue, [])
    return all_orders


if __name__ == '__main__':

    print(topsort_all([[0, 1], [1, 2]], 3))
    # expected:
    # [0, 1, 2]

    print(topsort_all([[3, 2], [3, 0], [2, 0], [2, 1]], 4))
    # expected:
    # 1) [3, 2, 0, 1]
    # 2) [3, 2, 1, 0]

    print(topsort_all([[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
                       ], 6))
    # expected:
    # 1) [0, 1, 4, 3, 2, 5]
    # 2) [0, 1, 3, 4, 2, 5]
    # 3) [0, 1, 3, 2, 4, 5]
    # 4) [0, 1, 3, 2, 5, 4]
    # 5) [1, 0, 3, 4, 2, 5]
    # 6) [1, 0, 3, 2, 4, 5]
    # 7) [1, 0, 3, 2, 5, 4]
    # 8) [1, 0, 4, 3, 2, 5]
    # 9) [1, 3, 0, 2, 4, 5]
    # 10) [1, 3, 0, 2, 5, 4]
    # 11) [1, 3, 0, 4, 2, 5]
    # 12) [1, 3, 2, 0, 5, 4]
    # 13) [1, 3, 2, 0, 4, 5]
