class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def PrintList(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    def Push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def Insert(self,prev,data):
        if prev == None:
            return 'Enter only existing node'
        new_node=Node(data)
        prev.next=new_node.next
        prev.next=new_node
    def Append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def Del(self,node):
        if node is None:
            return 'Enter existing node only'
        node.next=node.next.next
            
        
def main():
    L=LinkedList()
    L.Append(2)
    L.Insert(L.head,5)
    L.Insert(L.head.next,10)
    L.Push(0)
    L.Append(100)
   # L.Del(L.head.next.next)
    L.PrintList()
    
main()