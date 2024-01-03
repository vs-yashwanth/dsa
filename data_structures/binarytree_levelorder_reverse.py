from binarytree import BinaryTree
from queue_py import QueueRaw
from stack import StackRaw


def reverse_levelorder(root):
    if not root:
        return None
    queue = QueueRaw()
    queue.enqueue(root)
    out = [[root.val]]
    aux = []
    while not queue.is_empty():
        cur = queue.dequeue()
        if cur.left:
            aux.append(cur.left)
        if cur.right:
            aux.append(cur.right)
        if queue.is_empty() and aux:
            out.append([i.val for i in aux])
            for i in aux:
                queue.enqueue(i)
            aux = []
    rev = []
    for i in reversed(out):
        for j in i:
            rev.append(j)
    return rev


def reverse_levelorder_2(root):
    if not root:
        return None
    queue = QueueRaw()
    stack = StackRaw()
    queue.enqueue(root)
    while not queue.is_empty():
        cur = queue.dequeue()
        stack.push(cur.val)
        if cur.right:
            queue.enqueue(cur.right)
        if cur.left:
            queue.enqueue(cur.left)
    out = []
    while not stack.is_empty():
        out.append(stack.pop())
    return out


def print_level(root, level):
    if not root:
        return
    if level == 1:
        print(root.val, end=' ')
    elif level > 1:
        print_level(root.left, level-1)
        print_level(root.right, level-1)


if __name__ == '__main__':

    tree = BinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)

    print(reverse_levelorder(tree.root))  # 4 5 6 7 2 3 1
    print(reverse_levelorder_2(tree.root))  # 4 5 6 7 2 3 1
    h = tree.height()
    for i in reversed(range(1, h+2)):
        print_level(tree.root, i)
