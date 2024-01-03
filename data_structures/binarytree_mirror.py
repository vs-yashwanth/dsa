from binarytree import BinaryTree, TreeNode as Node


def mirror_tree(root):
    if not root:
        return
    mirror_tree(root.left)
    mirror_tree(root.right)
    root.left, root.right = root.right, root.left


def are_mirror_trees(root1, root2):
    if not root1 and not root2:
        return True
    elif not root1 or not root2:
        return False
    return root1.val == root2.val \
        and are_mirror_trees(root1.left, root2.right) \
        and are_mirror_trees(root1.right, root2.left)


if __name__ == '__main__':

    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)

    tree1 = BinaryTree()
    tree1.root = Node(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.left.left = Node(4)

    mirror_tree(tree.root)
    print(tree.inorder(tree.root))  # 3 1 2 4
    print(tree1.inorder(tree1.root))  # 4 2 1 3

    print(are_mirror_trees(tree1.root, tree.root))  # True
