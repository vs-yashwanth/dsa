class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    s=[root]
    while s:
        root = s.pop()
        print(root.data,end=' ')
        if root.right:
            s.append(root.right)
        if root.left:
            s.append(root.left)
    print()

def inorder(root):
    s = []
    temp = root
    while s or temp:
        if temp:
            s.append(temp)
            temp = temp.left
        else:
            temp = s.pop()
            print(temp.data,end=' ')
            temp = temp.right
    print()

def postorder(root):
    s1 = []
    s2 = []
    temp = root
    s1.append(temp)
    while s1:
        temp = s1.pop()
        s2.append(temp)
        if temp.left:
            s1.append(temp.left)
        if temp.right:
            s1.append(temp.right)
    while s2:
        print(s2.pop().data,end=' ')
    print()

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

