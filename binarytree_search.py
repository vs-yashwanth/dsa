class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def search(root,key):
    if not root:
        return False
    if root.data == key:
        return True
    return search(root.left,key) or search(root.right,key)

def search_iter(root,key):
    s = [root]
    while s:
        root = s.pop()
        if root.data == key:
            return True
        if root.left:
            s.append(root.left)
        if root.right:
            s.append(root.right)
    return False

root=Node(10)
root.left=Node(11)
root.right=Node(9)
root.left.left=Node(7)
root.right.left=Node(15)
root.right.right=Node(8)

print(search(root,15))
print(search_iter(root,16))