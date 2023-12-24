from binarytree import BinaryTree, TreeNode as Node

def max_path_sum(root):
    if not root:
        # path_sum going through root involving parent, max_path_sum of subtree at root
        return 0, -float('inf')
    left = max_path_sum(root.left)  # path_sum through the left child
    right = max_path_sum(root.right)  # path_sum through the right child
    max_here = root.val + left[0] + right[0]  # max_path_sum at current subtree
    return (max(root.val, root.val+max(left[0], right[0])), max(max_here, left[1], right[1]))
    # since path_sum through the root has to involve parent, it can only choose among 
    # one of its children, not both - or else the parent gets disconnected to the path


if __name__ == '__main__':

    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(2)
    tree.root.right = Node(10)
    tree.root.left.left = Node(20)
    tree.root.left.right = Node(1)
    tree.root.right.right = Node(-25)
    tree.root.right.right.left = Node(3)
    tree.root.right.right.right = Node(4)
    print(max_path_sum(tree.root)[1])
