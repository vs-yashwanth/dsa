from linkedlist_single import SingleLinkedList

def sum_lists(ll1,ll2):
    out = SingleLinkedList()
    ll1.reverse()
    ll2.reverse()
    cur1 = ll1.head
    cur2 = ll2.head
    carry = 0
    while cur1 or cur2:
        res = (cur1.val if cur1 else 0) + (cur2.val if cur2 else 0 )+ carry
        if res > 9:
            carry = res//10
            res = res%10
        else:
            carry = 0
        out.pushLeft(res)
        if cur1: cur1 = cur1.next
        if cur2: cur2 = cur2.next
    
    if carry:
        out.pushLeft(carry)

    return out


if __name__ == '__main__':
    ll1 = SingleLinkedList()
    ll2 = SingleLinkedList()

    ll1.push(1)
    ll1.push(2)
    ll1.push(3)
    ll1.push(4)
    ll2.push(4)
    ll2.push(3)
    ll2.push(2)
    ll2.push(1)

    ll3 = sum_lists(ll1,ll2)
    print(ll3)