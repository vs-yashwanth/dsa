class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def lappend(self,data):
        newnode=node(data)
        head=self.head
        newnode.next=head
        self.head=newnode
    def insert(self,prevnode,data):
        Nnode=node(data)
        Nnode.next=prevnode.next
        prevnode.next=Nnode
    def append(self,data):
        Nnode=node(data)
        last=self.head
        while last.next:
            last=last.next
        last.next=Nnode
    def dlt(self,prevnode):
        prevnode.next=prevnode.next.next



    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
def main():
    l=linkedlist()
    l.head=node(1)
    second=node(2)
    third=node(3)
    l.head.next=second
    second.next=third

    l.lappend(0)
    l.append('yes')
    l.dlt(l.head.next)
    l.insert(l.head.next.next,10)
    l.printlist()
main()