from binarytree import BinaryTree, TreeNode

def diameter(root):  # O(n^2)
    if not root:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return max(1+lh+rh, diameter(root.left), diameter(root.right))


def height(root):
    if not root:
        return 0
    return 1+max(height(root.left), height(root.right))

class Height:
    def __init__(self):
        self.h = 0

def diameter_2(root):

    height = Height()
    return diameter_aux(root, height)

def diameter_aux(root, height):
    if not root: return 0
    lh = Height()
    rh = Height()
    ld = diameter_aux(root.left, lh)
    rd = diameter_aux(root.right, rh)
    height.h = 1 + max(lh.h, rh.h)
    return max(ld, rd, 1+lh.h+rh.h)

if __name__ == '__main__':
    # Tree structure:
    #        5
    #       / \
    #      3   8
    #     / \   \
    #    2   4   10
    #   /       / \
    #  1       9   12

    tree = BinaryTree()
    tree.root = TreeNode(5)
    tree.root.left = TreeNode(3)
    tree.root.right = TreeNode(8)
    tree.root.left.left = TreeNode(2)
    tree.root.left.right = TreeNode(4)
    tree.root.left.left.left = TreeNode(1)
    tree.root.right.right = TreeNode(10)
    tree.root.right.right.left = TreeNode(9)
    tree.root.right.right.right = TreeNode(12)
    print(diameter(tree.root))
    print(diameter_2(tree.root))
