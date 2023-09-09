class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def levelorder(root):
    h=height(root)
    for i in range(1,h+1):
        print(currentlevel(root,i))
        
def currentlevel(root,i):
    if root is None:
        pass
    else:
        if i==1:
            print(root.data,end=' ')
        if i>1:
            currentlevel(root.left,i-1)
            currentlevel(root.right,i-1)

def height(root):
    if root is None:
        return 0
    lheight=height(root.left)
    rheight=height(root.right)
    
    if lheight>=rheight:
        return lheight+1
    else:
        return rheight+1
    
root=Node(10)
root.left=Node(11)
root.right=Node(9)
root.left.left=Node(7)
root.right.left=Node(15)
root.right.right=Node(8)

levelorder(root)
            