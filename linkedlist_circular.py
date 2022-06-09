class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def push(last,data):
    newnode = Node(data)
    newnode.next = last.next
    last.next  = newnode
    return last

def append(last,data):
    newnode=Node(data)
    newnode.next = last.next
    last.next = newnode
    return newnode

def insert(last,data,after):
    newnode = Node(data)
    temp = last.next
    while temp.data != after and temp is not last:
        temp = temp.next
    newnode.next = temp.next
    temp.next = newnode
    return last

def sorted_insert(last,data):
    newnode = Node(data)
    temp = last
    while temp.next.data < data and temp.next is not last:
        temp = temp.next
    if temp.next is last:
        newnode.next = last.next
        last.next = newnode
    else:
        newnode.next = temp.next
        temp.next = newnode
    if temp.next is last:
        return newnode
    else:
        return last
    

def count(tail):
    temp = tail
    count = 1
    while temp.next is tail:
        temp = temp.next
        count+=1
    return count

def show(tail):
    temp = tail.next
    while temp is not tail:
        print(temp.data,end=' ')
        temp = temp.next
    print(temp.data, end=' ')
    print()

def main():
    a = Node(1)
    b = Node(2)
    a.next = b
    c = Node(3)
    b.next = c
    d = Node(4)
    c.next = d
    d.next = a
    print(count(d))
    show(d)
    d = push(d,0)
    show(d)
    d = append(d,5)
    show(d)
    d =  insert(d,2.5,2)
    show(d)
    d = sorted_insert(d,3.3)
    show(d)
    d = sorted_insert(d,6)
    show(d)
    

main()