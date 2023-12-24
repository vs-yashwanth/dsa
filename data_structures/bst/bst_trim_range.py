from bst import BinarySearchTree

# trim the tree to contain only the values
# within given range


def trim_range(root, l, r):
    if not root:
        return None

    root.left = trim_range(root.left, l, r)
    root.right = trim_range(root.right, l, r)

    if l <= root.val <= r:
        return root
    if root.val < l:
        return root.right
    if root.val > r:
        return root.left

    return root


if __name__ == '__main__':

    bst = BinarySearchTree()

    # Insert nodes to create a binary search tree
    bst.insert(bst.root, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 40)
    bst.insert(bst.root, 70)
    bst.insert(bst.root, 60)
    bst.insert(bst.root, 80)

    bst.root = trim_range(bst.root, 11, 65)
    print(bst.inorder(bst.root))  # expected: 20 30 40 50 60
