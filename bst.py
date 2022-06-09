from binarytree import build

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def search(root,key):
    if root is None or root.data == key:
        return root
    if root.data<key:
        return search(root.right,key)
    else:
        return search(root.left,key)

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

def min_node(root):
    current=root
    while current.left:
        current=current.left
    return current

def delete(root,key):
    if root is None:
        return root
    if root.data<key:
        root.right=delete(root.right,key)
    elif root.data>key:
        root.left=delete(root.left,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        
        temp=min_node(root.right)
        root.data=temp.data
        root.right=delete(root.right,temp.data)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)
        

def levelorder(root):
    l=[]
    if root:
        q=[root]
        while q:
            temp=q.pop(0)
            l.append(temp.data)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
    return l

if __name__ == '__main__':
    

    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)
    

    inorder(root)
    print(build(levelorder(root)))

    root = delete(root, 20)

    inorder(root)
    print()

    root = delete(root, 30)

    inorder(root)

    print()
    root = delete(root, 50)

    inorder(root)
    print()






