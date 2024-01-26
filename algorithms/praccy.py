import networkx as nx

g3 = nx.Graph()
g3.add_edge(0, 1)
g3.add_edge(1, 2)
g3.add_edge(2, 0)
g3.add_edge(1, 3)
g3.add_edge(1, 4)
g3.add_edge(1, 6)
g3.add_edge(3, 5)
g3.add_edge(4, 5)
articulation_points = list(nx.articulation_points(g3))

print("Articulation Points:", articulation_points)
