class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

class B_LL:
    def __init__(self):

        self.head = self.tail = None
    
    def convert(self,root):
        if not root:
            return 
        self.convert(root.left)

        temp = root
        if not self.head:
            self.head = temp
        else:
            self.tail.right = temp
            temp.left = self.tail
        self.tail = temp
        
        self.convert(root.right)

        return root
    
    def show(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.right

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    ll = B_LL()
    root=ll.convert(root)
    ll.show()