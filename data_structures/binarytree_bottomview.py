class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        self.hd = 0

class Tree:
    def __init__(self):
        self.root = None
    
    def bottomview(self):
        temp = self.root
        q = [temp]
        map = {}
        hd = 0
        temp.hd = hd

        while q:
            temp = q.pop(0)
            map[temp.hd] = temp.data
            if temp.left:
                temp.left.hd = temp.hd -1 
                q.append(temp.left)
            if temp.right:
                temp.right.hd = temp.hd + 1
                q.append(temp.right)
        
        for i in sorted(map):
            print(map[i],end=' ')
        print()


if __name__=='__main__':
     
    root = Node(20)
    T = Tree()
    T.root = root
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
          
    T.bottomview()