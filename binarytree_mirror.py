from binarytree import Node, build
                         


def mirror(root):

    if not root:
        return
    mirror(root.left)
    mirror(root.right)
    root.left,root.right = root.right,root.left

def is_mirror(r1,r2):
    if not r1 and not r2:
        return True
    if not r1 or not r2:
        return False
    return r1.value==r2.value and is_mirror(r1.left,r2.right) and is_mirror(r1.right,r2.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(2)

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(2)

print(root)
print(root1)
mirror(root)
print(root)
print(root1)
print(is_mirror(root,root1))



