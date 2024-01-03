from binarytree import BinaryTree, TreeNode as Node

# the node which has one val in its left subtree
# and another in its right is the lca


def lca(root, v1, v2):
    if not root:
        return root
    if root.val == v1 or root.val == v2:
        return root
    left = lca(root.left, v1, v2)
    right = lca(root.right, v1, v2)
    return root if left and right else left or right


if __name__ == '__main__':

    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print("LCA(4,5) = ", lca(tree.root, 4, 5).val)
    print("LCA(4,6) = ", lca(tree.root, 4, 6).val)
    print("LCA(3,4) = ", lca(tree.root, 3, 4).val)
    print("LCA(2,4) = ", lca(tree.root, 2, 4).val)
