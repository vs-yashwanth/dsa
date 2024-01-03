from bst import BinarySearchTree, Node
from linkedlist_single import SingleLinkedList


def linkedlist_to_bst_1(head):  # O(nlogn)
    if not head:
        return head
    if not head.next:
        return Node(head.val)
    slow = fast = head
    prev = None
    while fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    mid = slow
    prev.next = None
    root = Node(mid.val)
    root.left = linkedlist_to_bst_1(head)
    root.right = linkedlist_to_bst_1(mid.next)
    return root


head = None


def linkedlist_to_bst_2(n):  # O(n), O(n)
    global head
    if n <= 0:
        return None
    left = linkedlist_to_bst_2(n//2)
    root = Node(head.val)
    root.left = left
    head = head.next
    root.right = linkedlist_to_bst_2(n-n//2-1)
    return root


def linkedlist_to_bst_3(head, n):  # O(n), O(n)
    if n <= 0:
        return None, head
    left, head = linkedlist_to_bst_3(head, n//2)
    root = Node(head.val)
    root.left = left
    head = head.next
    root.right, head = linkedlist_to_bst_3(head, n-n//2-1)
    return root, head


if __name__ == "__main__":

    fn = linkedlist_to_bst_2

    bst = BinarySearchTree()
    ll = SingleLinkedList()
    ll.push(20)
    ll.push(30)
    ll.push(40)
    ll.push(50)
    ll.push(60)
    ll.push(70)
    ll.push(80)
    head = ll.head
    root = fn(ll.length())
    print(bst.inorder(root))  # expected: [20, 30, 40, 50, 60, 70, 80]

    fn = linkedlist_to_bst_3
    bst = BinarySearchTree()
    ll = SingleLinkedList()
    ll.push(20)
    ll.push(30)
    ll.push(40)
    ll.push(50)
    ll.push(60)
    ll.push(70)
    ll.push(80)

    root, _ = fn(ll.head, ll.length())
    print(bst.inorder(root))  # expected: [20, 30, 40, 50, 60, 70, 80]
