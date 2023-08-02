#notworking
class Node:
    def __init__(self,data):
        self.data=data
        self.next = self.prev = None
    
def middle(head):

    temp=temp2=head
    while temp2 and temp2.next:
        temp2=temp2.next.next
        temp=temp.next
    return temp

def convert(head):
    if head is None or head.next is None:
        return head
    else:
        mid = middle(head)
        temp = head
        while temp.next != mid:
            temp=temp.next
        temp.next = None
        q = mid.next
        mid.next = None
        mid.prev = convert(head)
        mid.next = convert(q)
        return mid

def push(head,data):
    new=Node(data)
    if not head:
        return new
    new.next=head
    head.prev=new
    return new

def show(head):
    temp=head
    while temp:
        print(temp.data,end=' ')
        temp=temp.next
    print()

def pre(root):
    if root:
        print(root.data,end=' ')
        pre(root.prev)
        pre(root.next)

head=push(None,5)
head=push(head,4)
head=push(head,3)
head=push(head,2)
head=push(head,1)

show(head)
root=convert(head)
pre(root)


