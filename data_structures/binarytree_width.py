class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
    
def width(root):
    q = [root]
    m = -1

    while q:
        l = len(q)
        m = max(m,l)
        temp = q.pop(0)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    return m

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)

print(width(root))