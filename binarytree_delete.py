class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def delete(root):
    if not root:
        return
    root.left = delete(root.left)
    root.right = delete(root.right)
    root = None
    return root
    

def preorder(root):
    if root:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)

    
root=Node(10)
root.left=Node(11)
root.right=Node(9)
root.left.left=Node(7)
root.right.left=Node(15)
root.right.right=Node(8)

preorder(root)
print()
root = delete(root)
preorder(root)