class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Graph:
    def __init__(self,v):
        self.vertices=v
        self.G=[None]*self.vertices
    def add_edge(self,src,des):
        n=Node(des)
        n.next=self.G[src]
        self.G[src]=n
        
        n=Node(src)
        n.next=self.G[des]
        self.G[des]=n
    def show(self):
        for i,n in enumerate(self.G):
            print('The adjacency list of vertice {} is: '.format(i),end='')
            temp=n
            while temp:
                print(temp.data, end=' ')
                temp=temp.next
            print()

V = 5
graph = Graph(V)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
 
graph.show()
 
    