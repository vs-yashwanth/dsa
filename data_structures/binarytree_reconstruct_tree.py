from binarytree import BinaryTree, TreeNode as Node

# the nodes on the left of root in inorder represent the left sub tree
# and the this number of nodes after root in preorder represent the same
# and this number of nodes from start in postorder represent the left subtree


def construct1(preorder, inorder):
    if not preorder or not inorder:
        return None
    root_val = preorder[0]
    node = Node(root_val)
    root_ind = inorder.index(root_val)
    node.left = construct1(preorder[1:root_ind+1], inorder[:root_ind])
    node.right = construct1(preorder[root_ind+1:], inorder[root_ind+1:])
    return node


def construct2(postorder, inorder):
    if not postorder or not inorder:
        return None
    root_val = postorder[-1]
    node = Node(root_val)
    root_ind = inorder.index(root_val)
    node.left = construct2(postorder[:root_ind], inorder[:root_ind])
    node.right = construct2(postorder[root_ind:-1], inorder[root_ind+1:])
    return node


if __name__ == '__main__':
    preorder = ['A', 'B', 'D', 'E', 'C', 'F']
    inorder = ['D', 'B', 'E', 'A', 'F', 'C']
    postorder = ['D', 'E', 'B', 'F', 'C', 'A']

    tree = BinaryTree()
    tree.root = construct1(preorder, inorder)
    print(tree.preorder(tree.root))

    tree.root = construct2(postorder, inorder)
    print(tree.postorder(tree.root))
