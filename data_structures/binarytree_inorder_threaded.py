# not working
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        self.rthread = False

def leftmost(root):
    if not root:
        return root
    while root.left:
        root = root.left
    return root

def inorder(root):
    current = leftmost(root)
    while current:
        print(current.data, end =' ')

        if current.rthread:
            current = current.right
        else:
            current = leftmost(current.right)
    
root=Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)


inorder(root)