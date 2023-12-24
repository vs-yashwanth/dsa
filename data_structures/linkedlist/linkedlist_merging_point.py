from linkedlist_single import SingleLinkedList

# ideas

# -> comparing each next pointer to the next pointers of other - O(mn), O(1)
# -> store first nexts in a hashmap and lookup for the second - O(n), O(n)
# -> push the lists to separate stacks and pop them together till
#       we find a common node -> O(n), O(n)
# -> sort the first and lookup second nexts with binary search - O(nlogn), O(1)

# -> * move larger list ahead by the length difference and step - O(n), O(1)


def find_merging_point(ll1,ll2):
    l1 = ll1.length()
    l2 = ll2.length()
    d = abs(l1-l2)
    larger, smaller = (ll1,ll2) if l1 > l2 else (ll2,ll1)
    cur1 = larger.head
    for _ in range(d):
        cur1 = cur1.next
    cur2 = smaller.head
    while cur1 and cur2 and cur1.val != cur2.val:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1.val

if __name__ == '__main__':

    ll1 = SingleLinkedList()
    ll2 = SingleLinkedList()

    ll1.push(1)
    ll1.push(2)
    ll1.push(3)
    ll1.push(4)
    ll1.push(5)
    ll1.push(6)

    ll2.push(-3)
    ll2.push(-2)
    ll2.push(-1)
    ll2.push(0)
    ll2.head.next.next.next.next = ll1.head.next.next.next 

    print(find_merging_point(ll1,ll2))
    # expected output: 4   

    