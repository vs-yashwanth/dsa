from binarytree import BinaryTree


def path_sum_exists(root, target):
    if not root:
        return True if target == 0 else False
    target -= root.val
    if target == 0 and not root.left and not root.right:
        return True
    else:
        return path_sum_exists(root.left, target) or path_sum_exists(root.right, target)


if __name__ == '__main__':

    tree = BinaryTree()
    tree.insert(10)
    tree.insert(8)
    tree.insert(2)
    tree.insert(3)
    tree.insert(5)
    tree.insert(2)
    print(path_sum_exists(tree.root, 23)) # Expected: True
    print(path_sum_exists(tree.root, 3)) # Expected: False
