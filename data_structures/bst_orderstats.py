class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
count = 1

def n_smallest(root,n):
    global count
    if root:
        left = n_smallest(root.left,n)
        if left:
            return left
        if n==count:
            return root.data
        else:
            count += 1
        
        right = n_smallest(root.right,n)
        if right:
            return right

def insert(root,key):
    if root is None:
        return Node(key)
    if root.data==key:
        return root
    if root.data<key:
        root.right = insert(root.right,key)
    else:
        root.left = insert(root.left,key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)

root = None
keys = [ 20, 8, 22, 4, 12, 10, 14 ]

for x in keys:
    root = insert(root, x)
print(inorder(root))

print(n_smallest(root,2))

    