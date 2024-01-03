class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def enqueue(self,data):
        new = Node(data)
        if self.head is None :
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
    def dequeue(self):
        temp = self.head.data
        self.head = self.head.next
        return temp
    def peek(self):
        return self.head.data
    def show(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' ')
            temp = temp.next
        print()

if __name__ == '__main__':
    q = Queue()
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.show()
    print(q.dequeue())
    q.show()          
    