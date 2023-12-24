# path from root to each leaf is a leaf path
# leaf paths represent a number
# sum of those numbers
from binarytree import BinaryTree


def leafpath_sum(root, path_sum=0, paths=[]):
    if not root:
        return 0
    path_sum = path_sum*10 + root.val
    if root.left:
        leafpath_sum(root.left, path_sum, paths)
    if root.right:
        leafpath_sum(root.right, path_sum, paths)
    if not root.left and not root.right:
        paths.append(path_sum)
    return sum(paths)


if __name__ == '__main__':

    tree = BinaryTree()
    tree.insert(1)
    tree.insert(8)
    tree.insert(2)
    tree.insert(3)
    tree.insert(5)
    tree.insert(7)
    print(leafpath_sum(tree.root))
    # expected: 183+185+127 = 495