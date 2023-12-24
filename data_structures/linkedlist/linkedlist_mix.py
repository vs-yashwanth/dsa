
from linkedlist_single import SingleLinkedList

def mix_lists(ll1, ll2):
    cur1 = ll1.head
    cur2 = ll2.head
    if not cur1:
        return cur2
    elif not cur2:
        return cur1

    while cur1:
        nxt1 = cur1.next
        nxt2 = cur2.next
        cur1.next = cur2
        cur2.next = nxt1
        cur1 = nxt1
        cur2 = nxt2
        if not cur2:
            break

    if not cur1 and cur2:
        while cur2:
            ll1.push(cur2.val)
            cur2 = cur2.next

    return ll1.head


if __name__ == '__main__':

    ll1 = SingleLinkedList()
    ll2 = SingleLinkedList()
    ll1.push(1)
    ll1.push(2)
    ll1.push(3)
    ll1.push(4)
    ll2.push('a')
    ll2.push('b')
    ll2.push('c')
    ll2.push('d')
    ll2.push('e')
    ll1.head = mix_lists(ll1, ll2)
    print(ll1)
