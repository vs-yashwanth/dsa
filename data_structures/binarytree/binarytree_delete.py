from binarytree import BinaryTree


def delete(root):
    if not root:
        return
    root.left = delete(root.left)
    root.right = delete(root.right)
    del root
    return None


if __name__ == '__main__':

    tree = BinaryTree()
    tree.insert(1)
    tree.insert(8)
    tree.insert(4)
    tree.insert(7)
    tree.insert(3)

    print(tree.inorder(tree.root))
    print()
    tree.root = delete(tree.root)
    print(tree.inorder(tree.root))
