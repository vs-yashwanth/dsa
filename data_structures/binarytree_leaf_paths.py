# paths from root to leaves
from binarytree import BinaryTree


def leaf_paths(root, path=[]):
    if not root:
        return
    path.append(root.val)
    if root.left:
        leaf_paths(root.left, path.copy())
    if root.right:
        leaf_paths(root.right, path.copy())
    if not root.left and not root.right:
        print(path)


if __name__ == '__main__':

    tree = BinaryTree()
    tree.insert(10)
    tree.insert(8)
    tree.insert(2)
    tree.insert(3)
    tree.insert(5)
    tree.insert(7)
    leaf_paths(tree.root)
    # expected: 10,8,3 ; 10,8,5 ; 10,2,7
