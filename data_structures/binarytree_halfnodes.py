class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def half_nodes(root):
    q=[root]
    c = 0
    while q:
        temp = q.pop(0)
        if temp.left:
            q.append(temp.left)
            if not temp.right:
                c += 1
        if temp.right:
            q.append(temp.right)
            if not temp.left:
                c += 1
    return c


root=Node(10)
root.left=Node(11)
root.right=Node(9)
root.left.left=Node(7)
root.right.left=Node(15)
root.right.right=Node(8)

print(half_nodes(root))