class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def construct(ino,posto,in_s,in_e):
    global post

    if in_s>in_e:
        return None
    
    data = posto[post]
    temp = Node(data)
    post -= 1

    if in_s == in_e:
        return temp
    
    in_i = ino.index(data)
    temp.right = construct(ino,posto,in_i+1,in_e)
    temp.left = construct(ino,posto,in_s,in_i-1)

    return temp

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)

ino = [4, 8, 2, 5, 1, 6, 3, 7]
posto = [8, 4, 5, 2, 6, 7, 3, 1]
n = len(ino)
post = n-1

root = construct(ino, posto, 0,n-1)

inorder(root)