class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def identical(root1,root2):
    if not root1 and not root2:
        return True
    elif root1 and root2:
        return (root1.data == root2.data 
                and identical(root1.left,root2.left)
                and identical(root1.right,root2.right) )
    else:
        return False


root=Node(10)
root.left=Node(11)
root.right=Node(9)
root.left.left=Node(7)
root.right.left=Node(15)
root.right.right=Node(8)

root1=Node(10)
root1.left=Node(11)
root1.right=Node(9)
root1.left.left=Node(7)
root1.right.left=Node(15)
root1.right.right=Node(8)

print(identical(root,root1))