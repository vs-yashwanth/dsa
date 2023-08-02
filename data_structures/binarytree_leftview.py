class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.maxlevel = 0

    def leftview_level(self):
        temp = self.root
        print(temp.data,end=' ')
        q = [temp]
        q1 = []
        while q:
            temp = q.pop(0)
            if temp.left:
                q1.append(temp.left)
            if temp.right:
                q1.append(temp.right)
            if not q:
                q = q1.copy()
                if q:
                    print(q[0].data,end=' ')
                q1= []
    
    def leftview_recursive(self,root,level):

        if not root:
            return 
        
        if self.maxlevel < level:
            print(root.data,end=' ')
            self.maxlevel = level
        
        self.leftview_recursive(root.left,level+1)
        self.leftview_recursive(root.right,level+1)


if __name__ == '__main__':

    root = Node(12)
    T = Tree()
    T.root = root
    root.left = Node(10)
    root.right = Node(20)
    root.right.left = Node(25)
    root.right.right = Node(40)

    T.leftview_recursive(root,1)
    print()
    T.leftview_level()

    
 