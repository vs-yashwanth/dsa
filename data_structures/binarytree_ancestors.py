from binarytree import BinaryTree, TreeNode as Node


def ancestors(root, val, out=[]):
    if not root:
        return False
    if root.val == val:
        return True
    if ancestors(root.left, val, out) or ancestors(root.right, val, out):
        out.append(root.val)
        return True
    return False

if __name__ == '__main__':

    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.left.left.left = Node(7)
    
    anc = []
    ancestors(tree.root, 7, anc)
    print(anc)

