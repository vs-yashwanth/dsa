class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedList:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    def push(self,data):        # new head
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insertafter(self,prev,data):
        if prev is None:
            print('prev node must be valid')
        else:
            new_node=Node(data)
            new_node.next=prev.next
            prev.next=new_node
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
    def delete(self,key):
        if self.head is None:
             print('List is empty')
        if self.head.data == key:
            self.head = self.head.next
        else:
                
            temp=self.head
            while temp:
                 if temp.data==key:
                     break
                 prev=temp
                 temp=temp.next
            prev.next=temp.next
            temp=None
    
    def length(self):
        count=0
        temp=self.head
        while temp:
            count+=1
            temp=temp.next
        return count
    
    def search(self,key):
        found=False
        temp=self.head
        while temp:
            if temp.data==key:
                found=True
            temp=temp.next
        return found
        
            
        
l=linkedList()
l.head=Node(1)
sec=Node(2)
th=Node(3)
l.head.next=sec
sec.next=Node(3)
l.push(4)
l.push(5)
l.insertafter(l.head,0)
l.insertafter(l.head.next, 6)
l.append(7)
l.append(8)
l.printlist()
print('length ',l.length())
print('6',l.search(6))
l.delete(6)
l.delete(5)
print()
l.printlist()
print('length ',l.length())
print('6',l.search(6))