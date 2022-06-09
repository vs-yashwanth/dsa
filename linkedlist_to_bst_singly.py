class list_node:
    def __init__(self,data):
        self.data=data
        self.next=None
class bst_node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def convert(head):
    if not head:
        return head
    root=bst_node(head.data)
    q=[root]
    head=head.next
    while head:
        temp=q.pop(0)
        
        if head: 
            new = bst_node(head.data)
            temp.left = new
            q.append(temp.left)
            head=head.next
        if head:
            new = bst_node(head.data)
            temp.right = new
            q.append(temp.right)
            head = head.next
    return root

def push( head,new_data):

    # Creating a new linked list node and storing data
    new_node = list_node(new_data)

    # Make next of new node as head
    new_node.next = head

    # Move the head to point to new node
    head = new_node
    return new_node

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)

def traverse(head):
    while head:
        print(head.data,end=' ')
        head=head.next
    print()

head=None
head = push(head,36)
head = push(head,30)
head = push(head,25)
head = push(head,15)
head = push(head,12)
head = push(head,10)

traverse(head)
root=convert(head)
inorder(root)
        
