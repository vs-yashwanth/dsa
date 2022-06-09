class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)
    

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=' ')
    
def levelorder(root):
    if root:
        q=[root]
        while q:
            temp=q.pop(0)
            print(temp.data,end=' ')
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        
            
    

root=Node(10)
root.left=Node(11)
root.right=Node(9)
root.left.left=Node(7)
root.right.left=Node(15)
root.right.right=Node(8)

inorder(root)
print()
preorder(root)
print()
postorder(root)
print()
levelorder(root)
print()