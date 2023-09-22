class DisjointSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, data):  # O(1)
        # path compression
        if self.parent[data] != data:
            self.parent[data] = self.find(self.parent[data])
        return self.parent[data]

    def union(self, s1, s2):
        # union by rank   # O(1)
        r1 = self.find(s1)
        r2 = self.find(s2)
        if r1 == r2:
            return
        if self.rank[r1] < self.rank[r2]:
            self.parent[r1] = r2
        elif self.rank[r1] > self.rank[r2]:
            self.parent[r2] = r1
        else:
            self.parent[r2] = r1
            self.rank[r1] += 1


if __name__ == "__main__":
    S = DisjointSet(5)

    S.union(0, 1)
    S.union(2, 3)
    S.union(1, 4)

    print(S.find(0) == S.find(4))   # True
    print(S.find(1) == S.find(2))   # False
    print(S.find(2) == S.find(3))   # True

    S.union(2, 4)
    print(S.find(2) == S.find(1))   # True
