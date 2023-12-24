from bst import BinarySearchTree


def pred_succ(bst, key):
    inorder = bst.inorder(bst.root)
    n = len(inorder)
    i = 0
    while i < n:
        if inorder[i] == key:
            if i-1 >= 0 and i+1 < n:
                return (inorder[i-1], inorder[i+1])
            else:
                return None
        i += 1


pred, succ = None, None


def pred_succ_2(root, key):
    global pred, succ
    if not root:
        return None

    pred_succ_2(root.left, key)
    if root.val == key:
        pred = max_node(root.left).val
        succ = min_node(root.right).val
    pred_succ_2(root.right, key)
    return pred, succ if pred and succ else None


def min_node(root):

    while root and root.left:
        root = root.left
    return root


def max_node(root):
    while root and root.right:
        root = root.right
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

    print(pred_succ(bst, 30))

    print(pred_succ_2(bst.root, 50))
