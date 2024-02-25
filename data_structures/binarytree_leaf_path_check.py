from binarytree import BinaryTree

# check if the given sequence is a leaf path


def is_leaf_path(root, seq, i):  # O(n), O(h)
    if not root or i >= len(seq):
        return False
    if int(seq[i]) == root.val:
        if not root.left and not root.right and i == len(seq)-1:
            return True
        return is_leaf_path(root.left, seq, i+1) \
            or is_leaf_path(root.right, seq, i+1)

    return False


if __name__ == '__main__':

    tree = BinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    tree.insert(9)
    tree.insert(10)
    tree.insert(11)
    tree.insert(12)
    # print(tree.levels())

    print(is_leaf_path(tree.root, [1, 2, 4, 9], 0))  # True
    print(is_leaf_path(tree.root, [1, 2, 5, 8], 0))  # False
    print(is_leaf_path(tree.root, [1, 3, 6, 12], 0))  # True
    print(is_leaf_path(tree.root, [1, 2, 5, 11], 0))  # True
    print(is_leaf_path(tree.root, [1], 0))        # False
    print(is_leaf_path(tree.root, [1, 3, 6, 12, 13], 0))  # False
