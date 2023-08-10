class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    
    def append(self,data):
        newnode = Node(data)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode
        else:
            self.head = newnode
    
    def insert(self,data,prev):
        
        newnode = Node(data)
        if not prev:
            raise "None error"
        else:
            newnode.next = prev.next
            prev.next = newnode
        
    def delete_node(self,key):
        temp = self.head
        if temp.data == key:
            self.head = temp.next
        else:
            while temp.next.data != key:
                temp = temp.next
            temp.next = temp.next.next
    
    def delete_recursive(self,head,key):
        if not head or head.data == key:
            self.head = None
            
        if not head.next:
            return
        else:
            if head.next.data != key:
                self.delete_recursive(head.next,key)
            else:
                head.next = head.next.next
                
    def delete_pos(self,pos):
        if pos == 0:
            self.head = None
        else:     
            temp = self.head
            for _ in range(pos-1):
                temp = temp.next
            temp.next = temp.next.next
        
    def reverse_iter(self):
        prev = None
        temp = self.head
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        self.head = prev
    
    def reverse_recursive(self,head):
        if not head or not head.next:
            return head
        rest = self.reverse_recursive(head.next)
        head.next.next = head
        head.next = None
        return rest
    
    def reverse_recursive2(self,prev,temp):
        if not temp.next:
            self.head = temp
            temp.next = prev
            return
        nxt = temp.next
        temp.next = prev
        self.reverse_recursive2(temp,nxt)
    
    def reverse_stack(self):
        s = []
        temp = self.head
        while temp:
            s.append(temp)
            temp = temp.next
        self.head = temp = s.pop()
        while s:
            temp.next = s.pop()
            temp = temp.next
        temp.next = None
        
    def reverse_k(self,head,k):
        if not head:
            return head
        temp = head
        prev = nxt = None
        count = 0
        
        while temp and count<k:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
            count += 1
        if nxt:
            head.next = self.reverse_k(nxt,k)
        return prev
    
    def merge(self,h1,h2):
        
        dummy = Node(0)
        tail = dummy
        while True:
            if not h1:
                tail.next = h2
                break
            if not h2:
                tail.next = h1
                break
            if h1.data < h2.data:
                tail.next = h1
                h1 = h1.next
            else:
                tail.next = h2
                h2 = h2.next
            tail = tail.next
        return dummy.next

    def merge2(self,h1,h2):
        temp = None
        if not h1:
            return h2
        if not h2:
            return h1
        if h1.data <= h2.data:
            temp = h1
            temp.next = self.merge2(h1.next,h2)
        else:
            temp = h2
            temp.next =self.merge2(h1,h2.next)
        return temp
    
    def middle(self,head):
        if not head:
            return head
        else:
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
    def mergesort(self,head):
        if not head or not head.next:
            return head
        middle = self.middle(head)
        middle_next = middle.next
        middle.next = None
        left = self.mergesort(head)
        right = self.mergesort(middle_next)
        sortedlist = self.merge2(left,right)
        return sortedlist

    def length(self):
        temp = self.head
        l=0
        while temp:
            l+=1
            temp = temp.next
        return l
    
    def length_recursive(self,head):
        if not head:
            return 0
        else:
            return 1 + self.length_recursive(head.next)
    
    def swap(self,x,y):
        if x == y:
            return 
        xprev = None
        xnow = self.head
        while xnow and xnow.data != x:
            xprev = xnow
            xnow = xnow.next
        yprev = None
        ynow = self.head
        while ynow and ynow.data != y:
            yprev = ynow
            ynow = ynow.next
        
        if not xnow or not ynow:
            return 'not found'
        
        if xprev:
            xprev.next = ynow
        else:
            self.head = ynow
        if yprev:
            yprev.next = xnow
        else:
            self.head = xnow
        
        xnow.next, ynow.next = ynow.next, xnow.next
    
    def swap2(self,x,y):
        temp = self.head
        if x==y:
            return
        a=b=None
        while temp.next :
            if temp.next.data == x:
                a = temp
            elif temp.next.data == y:
                b = temp
            temp = temp.next
        
        if a and b:
            a.next, b.next = b.next, a.next
            a.next.next, b.next.next = b.next.next, a.next.next
        
    def __str__(self):
        temp = self.head
        r=''
        while temp:
            r =r +' '+ str(temp.data)
            temp = temp.next
        return r

if __name__ == '__main__' :
    
    l = LinkedList()
    l.head = Node(1)
    second = Node(2)
    l.head.next = second
    third = Node(3)
    second.next = third
    l.push(0)
    l.append(4)
    l.insert('e',l.head)
    print(l)
    l.delete_node('e')
    l.delete_recursive(l.head, 3)
    l.delete_pos(2)
    print(l)
    print('len:',l.length(),l.length_recursive(l.head))
    l.append(3)
    l.append(5)
    print(l)
    l.swap(4,3)
    print(l)
    l.swap2(5,4)
    print(l)
    l.reverse_iter()
    print(l)
    l.head = l.reverse_recursive(l.head)
    print(l)
    l.reverse_recursive2(None, l.head)
    print(l)
    l.reverse_stack()
    print(l)
    l1 = LinkedList()
    l1.head = Node(10)
    l1.push(2)
    l1.append(12)
    l1.head = l1.merge(l.head, l1.head)
    print(l1)
    l2 = LinkedList()
    l2.push(30)
    l2.push(20)
    l2.push(11)
    l2.head = l2.merge2(l2.head, l1.head)
    print(l2)
    l2.head = l2.mergesort(l2.head)
    print(l2)
    l2.head = l2.reverse_k(l2.head,3)
    print(l2)

        