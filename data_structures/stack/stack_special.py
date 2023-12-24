class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class specialstack:
    def __init__(self):
        self.top = None
        self.top2 = None
    
    def push(self,data):
        new = Node(data)
        new.next = self.top
        self.top = new
        
        new2 = Node(data)
        if not self.top2:
            self.top2 = new2
        else:
            new2 = new2 if new2.data<self.top2.data else self.top2
            self.top2 = new2
    
    def pop(self):
        temp = self.top
        self.top = self.top.next
        return temp.data
        
        self.top2 = self.top2.next
    
    def peek(self):
        return self.top.data
    
    def get_min(self):
        
        return self.top2.data
    
    def show(self):
        print('stack: ')
        temp = self.top
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        print()
        
        print('aux stack: ',self.get_min())
        
if __name__ == '__main__':
    s = specialstack()
    s.push(3)
    s.push(4)
    s.push(5)
    s.show()
    print(s.get_min())
    s.push(1)
    print(s.get_min())
    s.show()
    
        
        