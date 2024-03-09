# https://leetcode.ca/all/444.html

from collections import defaultdict, deque


def verify_unique_seq(og, seqs):  # O(n), O(n)

    graph = defaultdict(list)
    indegrees = defaultdict(int)
    nodes = set()
    queue = deque()
    order = []

    for seq in seqs:
        for i in range(len(seq)-1):
            nodes.add(seq[i])
            nodes.add(seq[i+1])
            graph[seq[i]].append(seq[i+1])
            indegrees[seq[i+1]] += 1

    for node in nodes:
        if indegrees[node] == 0:
            queue.append(node)

    while queue:
        if len(queue) > 1:
            return False
        cur = queue.popleft()
        order.append(cur)
        for neigh in graph[cur]:
            indegrees[neigh] -= 1
            if indegrees[neigh] == 0:
                queue.append(neigh)

    return order == og


if __name__ == '__main__':

    print(verify_unique_seq([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]]))  # True
    print(verify_unique_seq([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]]))  # False
    print(verify_unique_seq([3, 1, 4, 2, 5],
          [[3, 1, 5], [1, 4, 2, 5]]))  # True
    print(verify_unique_seq([1, 2, 3], [[1, 2], [1, 3]]))  # False
    print(verify_unique_seq([1, 2, 3], [[1, 2]]))  # False
    print(verify_unique_seq([1, 2, 3], [[1, 2], [1, 3], [2, 3]]))  # True
    print(verify_unique_seq([4, 1, 5, 2, 6, 3],
          [[5, 2, 6, 3], [4, 1, 5, 2]]))  # True
