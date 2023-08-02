class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
    
def kdistant(root,k):
    if not root or k<0:
        return
    if k==0:
        print(root.data)
    else:
        kdistant(root.left,k-1)
        kdistant(root.right,k-1)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(8)
 
print(kdistant(root, 2))