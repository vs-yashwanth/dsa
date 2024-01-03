class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def deepest(root):
    q=[root]
    while q:
        temp = q.pop(0)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    return temp.data


root=Node(10)
root.left=Node(11)
root.right=Node(9)
root.left.left=Node(7)
root.right.left=Node(15)
root.right.right=Node(8)
root.right.right.left = Node(100)

print(deepest(root))