class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(N):
    if N is not None:
        inorder(N.left)
        print(N.data,end=' ')
        inorder(N.right)

def insert(root,key):
    if root is None:
        root=Node(key)
    else:
        Q=[]
        Q.append(root)
        while len(Q):
            temp=Q.pop(0)
            if temp.left is None:
                temp.left=Node(key)
                break
            else:
                Q.append(temp.left)
            if temp.right is None:
                temp.right=Node(key)
                break
            else:
                Q.append(temp.right)

root=Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)
 
print("Inorder traversal before insertion:", end = " ")
inorder(root)
 
key = 12
insert(root, key)
 
print()
print("Inorder traversal after insertion:", end = " ")
inorder(root)
        