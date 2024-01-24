def topsort(self):

    visited = set()
    stack = []
    for i in self.nodes:
        if i not in visited:
            self.dfs(i, visited, stack)

    print(stack[::-1])

def dfs(self, s, visited, stack):
    visited.add(s)
    for j in self.g[s]:
        if j not in visited:
            self.dfs(j, visited, stack)
    stack.append(s)