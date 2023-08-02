import ctypes

class Node:
    def __init__(self,data):
        self.data = data
        self.xpn = 0
    
class xor_list:
    def __init__(self):
        self.head = None
        self.__nodes =[]
    
    def insert(self,data):
        new = Node(data)
        new.xpn = id(self.head)
        if self.head:
            self.head.xpn = id(new) ^ self.head.xpn
        self.head = new
        self.__nodes.append(new)
    
    def show(self):
        if self.head:
            prev=0
            curr=self.head
            next=1
            while curr:
                print(curr.data,end=' ')
                next = prev ^ id(curr)
                prev = id(curr)
                curr = ctypes.cast(next,ctypes.py_object).value

X = xor_list()
X.insert(10)
X.insert(20)
X.insert(30)
X.insert(40)

X.show()
            