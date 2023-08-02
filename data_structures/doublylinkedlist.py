class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
def push(head,data):
    newnode = Node(data)
    
    newnode.next = head
    head.prev = newnode
    
    return newnode

def append(head,data):
    newnode=  Node(data)
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newnode
    newnode.prev = temp
    return head

def insert(head,data,after):
    newnode=Node(data)
    temp=head
    while temp.data != after:
        temp = temp.next
    newnode.next = temp.next
    newnode.prev = temp
    temp.next.prev = newnode
    temp.next = newnode
    return head

def delleft(head):
    temp = head.next
    temp.prev = None
    return temp

def delright(head):
    temp = head
    while temp.next:
        temp = temp.next
    temp.prev.next = None
    return head

def delete(head,after):
    temp = head
    while temp.data != after:
        temp=temp.next
    temp.next.next.prev = temp
    temp.next = temp.next.next
    return head
    
def reverse(head):
    temp = head
    temp2 = temp.prev
    while temp:
        temp2 = temp.prev
        temp.prev = temp.next
        temp.next = temp2
        temp = temp.prev
    if temp2:
        return temp2.prev
    
def reverse_stack(head):
    stack = []
    temp = head
    while temp:
        stack.append(temp.data)
        temp=temp.next
    temp = head
    while temp:
        temp.data = stack.pop()
        temp = temp.next
    return head

def quicksort(head):
    tail=head
    while tail.next:
        tail = tail.next
    quicky(head,tail)

def quicky(head,tail):
    if (head is not tail) and ( tail is not None) and (head is not tail.next) :
        q = partition(head,tail)
        quicky(head,q.prev)
        quicky(q.next,tail)
def partition(head,tail):
    p = tail.data
    i = head.prev
    j = head
    while j.next is not tail:
        if j.data <= p:
            i = i.next
            i.data,j.data = j.data,i.data
        j = j.next
    if i:
        i = i.next
    else:
        i = head
    i.data, tail.data = tail.data, i.data
    return i

def print_dll(head):
    while head:
        print(head.data,end=' ')
        head = head.next
    print()
    
def main():
    head = Node(1)
    second = Node(2)
    head.next = second
    second.prev =  head
    third = Node(3)
    second.next = third
    third.prev = second
    print_dll(head)
    head = push(head,0)
    print_dll(head)
    head = append(head,4)
    print_dll(head)
    head = insert(head,2.5,2)
    print_dll(head)
    head = delleft(head)
    print_dll(head)
    head = delright(head)
    print_dll(head)
    head = delete(head,2)
    print_dll(head)
    head = reverse(head)
    print_dll(head)
    head = reverse_stack(head)
    print_dll(head)
    head = append(head,0)
    print_dll(head)   
    quicksort(head)
    print_dll(head)
    print('mergesort loading...')
main()