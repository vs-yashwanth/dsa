from bst import BinarySearchTree


def lca(root, n1, n2):
    if not root:
        return root
    if n1 < root.val and n2 < root.val:
        return lca(root.left, n1, n2)
    elif n1 > root.val and n2 > root.val:
        return lca(root.right, n1, n2)
    else:  # when n1 == root.val, n2 == root.val, n1 < root.val< n2, n1 > root.val > n2
        return root


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

    # Test case 1: LCA of 20 and 40 is 30
    lca1 = lca(bst.root, 20, 40)
    # Expected output: 30
    print("LCA of 20 and 40:", lca1.val)

    # Test case 2: LCA of 20 and 60 is 50
    lca2 = lca(bst.root, 20, 60)
    # Expected output: 50
    print("LCA of 20 and 60:", lca2.val)

    # Test case 3: LCA of 30 and 80 is 50
    lca3 = lca(bst.root, 30, 80)
    # Expected output: 50
    print("LCA of 30 and 80:", lca3.val)

    # Test case 4: LCA of 20 and 70 is 50
    lca4 = lca(bst.root, 20, 70)
    # Expected output: 50
    print("LCA of 20 and 70:", lca4.val)
