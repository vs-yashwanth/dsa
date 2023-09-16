from bst import BinarySearchTree


def kth_smallest(tree, k):
    inorder = tree.inorder(tree.root)
    return inorder[k-1]


def kth_largest(tree, k):
    inorder = tree.inorder(tree.root)
    return inorder[len(inorder)-k]


count = 0


def kth_smallest_2(root, k):
    global count
    if not root:
        return None
    out = kth_smallest_2(root.left, k)
    count += 1
    if count == k:
        return root.val
    return out or kth_smallest_2(root.right, k)


def kth_largest_2(root, k):

    def size(root):
        if not root:
            return 0
        return size(root.left) + 1 + size(root.right)

    count = size(root)

    def largest_helper(root, k):
        nonlocal count
        if not root:
            return root
        out = largest_helper(root.left, k)
        if count == k:
            return root.val
        count -= 1
        return out or largest_helper(root.right, k)
    return largest_helper(root, k)


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

    print(kth_smallest(bst, 2))  # expected: 30
    print(kth_largest(bst, 2))  # expected: 70

    print(kth_smallest_2(bst.root, 1))  # expected: 20
    print(kth_largest_2(bst.root, 1))  # expected: 80
