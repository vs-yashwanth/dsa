from bst import BinarySearchTree
from binarytree import BinaryTree, TreeNode


def check(root, min, max):  # O(n), O(n)
    if not root:
        return True
    if root.val >= max or root.val <= min:
        return False
    return check(root.left, min, root.val) \
        and check(root.right, root.val, max)


def check2(bst):  # O(n^2)
    return bst.inorder(bst.root) == sorted(bst.levelorder())


def check3(bst):  # O(n)
    inorder = bst.inorder(bst.root)
    for i in range(len(inorder)-1):
        if inorder[i] >= inorder[i+1]:
            return False
    return True


if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insert nodes to create a binary search tree
    bst.insert(bst.root, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 40)
    bst.insert(bst.root, 70)
    bst.insert(bst.root, 60)
    bst.insert(bst.root, 80)

    print(check(bst.root, -float('inf'), float('inf')))
    print(check2(bst))
    print(check3(bst))

    tree = BinaryTree()
    tree.root = TreeNode(5)
    tree.root.left = TreeNode(10)
    tree.root.right = TreeNode(8)
    tree.root.left.left = TreeNode(20)
    tree.root.left.right = TreeNode(4)
    tree.root.left.left.left = TreeNode(1)
    tree.root.right.right = TreeNode(10)
    tree.root.right.right.left = TreeNode(9)
    tree.root.right.right.right = TreeNode(12)

    print(check(tree.root, -float('inf'), float('inf')))
    print(check2(tree))
    print(check3(tree))
