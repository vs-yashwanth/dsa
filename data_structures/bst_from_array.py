# build bst from sorted array

from bst import BinarySearchTree, Node


def bst_from_array(array, left, right):
    if right < left:
        return None
    mid = (left+right)//2
    node = Node(array[mid])
    node.left = bst_from_array(array, left, mid-1)
    node.right = bst_from_array(array, mid+1, right)
    return node


if __name__ == "__main__":

    array = [20, 30, 40, 50, 60, 70, 80]
    bst = BinarySearchTree()
    root = bst_from_array(array, 0, len(array)-1)
    print(bst.inorder(root))
