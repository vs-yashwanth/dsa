class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def lca(root,k1,k2):
    if not root:
        return root
    if root.data==k2 or root.data==k1:
        return root
    left = lca(root.left,k1,k2)
    right=lca(root.right,k1,k2)
    if left and right:
        return root
    return left if left else right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print ("LCA(4,5) = ", lca(root, 4, 5).data)
print( "LCA(4,6) = ", lca(root, 4, 6).data)
print ("LCA(3,4) = ", lca(root, 3, 4).data)
print ("LCA(2,4) = ", lca(root, 2, 4).data)


