from bst import BinarySearchTree


def values_in_range(root, l, r, out=[]):
    if not root:
        return None
    values_in_range(root.left, l, r, out)
    if l <= root.val <= r:
        out.append(root.val)
    values_in_range(root.right, l, r, out)
    return out


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

    print(values_in_range(bst.root, 11, 65))
