from binarytree import Node
from binarytree import build

root=Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)


print(root)
print(root.height,root.size)
print(root.inorder)
print(root.preorder)
print(root.postorder)
print(root.levelorder)

