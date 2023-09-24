import random


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if not root:
            node = TreeNode(val)
            if not self.root:
                self.root = node
            return node

        if root.val == val:
            return
        if root.val > val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def inorder(self, root, out=[]):
        if root:
            self.inorder(root.left, out)
            out.append(root.val)
            self.inorder(root.right, out)
        return out


def tree_sort(array):
    bst = BST()
    for i in array:
        bst.insert(bst.root, i)
    return bst.inorder(bst.root)


if __name__ == '__main__':
    n = 6
    a = list(random.sample(range(1, 9), n))
    print(a)
    a_s = a.copy()
    a_s = tree_sort(a_s)
    print(a_s)
    print(a_s == sorted(a))
