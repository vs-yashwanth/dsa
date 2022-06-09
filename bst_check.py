class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_inorder(root):
    s=[]
    o=[]
    temp=root
    while s or temp:
        if temp:
            s.append(temp)
            temp=temp.left
        else:
            temp=s.pop()
            o.append(temp.data)
            temp=temp.right
    return o



def check1(root, mini, maxi):
    if not root:
        return True
    if root.data < mini or root.data > maxi:
        return False
    return check1(root.left, mini, root.data-1) and \
            check1(root.right,root.data+1, maxi)

def check2(root):
    inorder = get_inorder(root)
    return inorder == sorted(inorder)

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

print(check1(root,-float('inf'),float('inf')))
print(check2(root))