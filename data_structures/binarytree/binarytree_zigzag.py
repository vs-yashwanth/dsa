from binarytree import BinaryTree
from queue_py import QueueRaw


def zigzag(root):
    now = []
    next = []
    now.append(root)
    order = True
    while now:
        temp = now.pop()
        print(temp.val, end=' ')
        if order:
            if temp.left:
                next.append(temp.left)
            if temp.right:
                next.append(temp.right)
        else:
            if temp.right:
                next.append(temp.right)
            if temp.left:
                next.append(temp.left)
        if not now:
            order = not order
            now, next = next, now


def zigzag_levelorder(root):
    if not root:
        return []
    queue = QueueRaw()
    queue.enqueue(root)
    level = []
    order = False
    out = [root.val]
    while not queue.is_empty():
        cur = queue.dequeue()
        if cur.left:
            level.append(cur.left)
        if cur.right:
            level.append(cur.right)
        if queue.is_empty():
            if order:
                out += [i.val for i in level]
            else:
                out += [i.val for i in level[::-1]]
            for i in level:
                queue.enqueue(i)
            level = []
            order = not order
    return out


def print_levels(root):
    if not root:
        return
    queue = [root]
    aux = []
    while queue:
        cur = queue.pop(0)
        if cur.left:
            aux.append(cur.left)
        if cur.right:
            aux.append(cur.right)
        if not queue:
            print([i.val for i in aux])
            queue.extend(aux)
            aux = []


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    zigzag(tree.root)
    print()
    print(zigzag_levelorder(tree.root))
