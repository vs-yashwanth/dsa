from bst import BinarySearchTree

prev = None


def bst_to_dll(root):
    global prev
    if not root:
        return root
    head = bst_to_dll(root.left)
    if not prev:
        head = root
    else:
        root.left = prev
        prev.right = root
    prev = root
    bst_to_dll(root.right)
    return head


def bst_to_sll(root):
    global prev
    if not root:
        return root
    head = bst_to_sll(root.left)
    if not prev:
        head = root
    else:
        root.left = None
        prev.right = root
    prev = root
    bst_to_sll(root.right)
    return head


def bst_to_cll_1(root):
    global prev
    head = bst_to_dll(root)
    cur = head
    while cur.right:
        cur = cur.right
    cur.right = head
    head.left = cur
    return head


def bst_to_cll_2(root):
    if not root:
        return root

    left_list = bst_to_cll_2(root.left)
    right_list = bst_to_cll_2(root.right)

    root.left = root.right = root
    temp_head = concatenate_cll(left_list, root)
    head = concatenate_cll(temp_head, right_list)
    return head


def concatenate_cll(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    l1_last = l1.left
    l2_last = l2.left

    l1_last.right = l2
    l2.left = l1_last
    l2_last.right = l1
    l1.left = l2_last

    return l1


def traverse_dll(head):
    out = []
    out_rev = []
    cur = head
    prev = None
    while cur:
        out.append(cur.val)
        prev = cur
        cur = cur.right
    while prev:
        out_rev.append(prev.val)
        prev = prev.left
    return out, out_rev[::-1]


def traverse_sll(head):
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.right
    return out


def traverse_cll(head):
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.right
        if cur is head:
            break
    return out


if __name__ == "__main__":

    bst = BinarySearchTree()
    # Insert nodes to create a binary search tree
    bst.insert(bst.root, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 40)
    bst.insert(bst.root, 70)
    bst.insert(bst.root, 60)
    bst.insert(bst.root, 80)
    print(bst.inorder(bst.root))  # expected: 20 30 40 50 60 70 80
    head = bst_to_dll(bst.root)
    print(traverse_dll(head))  # expected: 20 30 40 50 60 70 80

    prev = None
    bst = BinarySearchTree()
    # Insert nodes to create a binary search tree
    bst.insert(bst.root, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 40)
    bst.insert(bst.root, 70)
    bst.insert(bst.root, 60)
    bst.insert(bst.root, 80)
    head = bst_to_sll(bst.root)

    print(traverse_sll(head))  # expected: 20 30 40 50 60 70 80

    prev = None
    bst = BinarySearchTree()
    # Insert nodes to create a binary search tree
    bst.insert(bst.root, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 40)
    bst.insert(bst.root, 70)
    bst.insert(bst.root, 60)
    bst.insert(bst.root, 80)
    head = bst_to_cll_1(bst.root)

    print(traverse_cll(head))  # expected: 20 30 40 50 60 70 80

    bst = BinarySearchTree()
    # Insert nodes to create a binary search tree
    bst.insert(bst.root, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 40)
    bst.insert(bst.root, 70)
    bst.insert(bst.root, 60)
    bst.insert(bst.root, 80)

    head = bst_to_cll_2(bst.root)
    print(traverse_cll(head))  # expected: 20 30 40 50 60 70 80
