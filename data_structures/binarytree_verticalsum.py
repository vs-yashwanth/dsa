from binarytree import BinaryTree
from collections import defaultdict


def vertical_sum(root, horizontal_dist, D):
    if not root:
        return 0
    if horizontal_dist in D:
        D[horizontal_dist] += root.val
    else:
        D[horizontal_dist] = root.val
    vertical_sum(root.left, horizontal_dist-1, D)
    vertical_sum(root.right, horizontal_dist+1, D)


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    d = {}
    vertical_sum(tree.root, 0, d)
    print([d[key] for key in sorted(d.keys())])
