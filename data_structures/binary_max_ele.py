from binarytree import BinaryTree
from queue_py import QueueRaw


def max_element(tree):   # O(n), O(n)
    root = tree.root
    if not root:
        return None
    max_ele = -1
    queue = QueueRaw()
    queue.enqueue(root)
    while not queue.is_empty():
        cur = queue.dequeue()
        max_ele = max(max_ele, cur.val)
        if cur.left:
            queue.enqueue(cur.left)
        if cur.right:
            queue.enqueue(cur.right)
    return max_ele


def max_element_recursion(root, max_val=-1):
    if not root:
        return max_val

    max_val = max(root.val, max_val, max_element_recursion(
        root.left), max_element_recursion(root.right))

    return max_val


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)
    tree.insert(16)
    tree.insert(13)
    tree.insert(10)
    print(max_element(tree))  # expected: 16
    print(max_element_recursion(tree.root)) # expected: 16
