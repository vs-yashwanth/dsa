class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def size(root):
    if not root:
        return 0
    return 1+size(root.left)+size(root.right)

def size_iter(root):
    s = [root]
    count = 0
    while s:
        root = s.pop()
        count += 1
        if root.left:
            s.append(root.left)
        if root.right:
            s.append(root.right)
    return count

root=Node(10)
root.left=Node(11)
root.right=Node(9)
root.left.left=Node(7)
root.right.left=Node(15)
root.right.right=Node(8)

print(size(root))
print(size_iter(root))