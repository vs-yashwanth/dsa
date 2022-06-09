class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        self.hd = 0

class Tree:
    def __init__(self):
        self.root = None
    
    def vertical_print(self):     # O(n)
        temp = self.root
        temp.hd = 0
        q = [temp]
        D = {}
        while q:
            temp = q.pop(0)
            if temp.hd not in D:
                D[temp.hd] = []
            D[temp.hd].append(temp.data)

            if temp.left:
                temp.left.hd = temp.hd - 1
                q.append(temp.left)
            
            if temp.right:
                temp.right.hd = temp.hd + 1
                q.append(temp.right)

        for i in sorted(D):
            print(D[i])
    

root = Node(1)
T = Tree()
T.root = root
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
 
T.vertical_print()
