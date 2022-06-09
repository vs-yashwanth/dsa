from typing import NoReturn


class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        self.height = 1

def height(root):
    if not root:
        return 0
    return root.height

def balance(root):
    if not root:
        return 0
    return height(root.left) - height(root.right)

def min_node(root):
    if not root: return root
    while root.left:
        root = root.left
    return root

def preorder(root):
    if root:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)

def left_rotate(root):
    temp1 = root.right
    temp2 = temp1.left

    temp1.left = root
    root.right = temp2

    temp1.height = 1+max(height(temp1.left), height(temp1.right))
    root.height = 1+max(height(root.left), height(root.right))

    return temp1

def right_rotate(root):
    temp1 = root.left
    temp2 = temp1.right

    temp1.right = root
    root.left = temp2

    temp1.height = 1+max(height(temp1.left), height(temp1.right))
    root.height = 1+max(height(root.left), height(root.right))

    return temp1

def insert(root,value):
    if not root:
        return Node(value)
    elif root.data < value:
        root.right = insert(root.right,value)
    else:
        root.left = insert(root.left,value)
    
    root.height = 1+max(height(root.left),height(root.right))
    bal = balance(root)

    if bal > 1 and value < root.left.data  :
        return right_rotate(root)
    if bal < -1 and value > root.right.data :
        return left_rotate(root)
    if bal > 1 and value > root.left.data :
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if bal < -1 and value < root.right.data :
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def delete(root,data):
    if not root:
        return root
    if data < root.data:
        root.left = delete(root.left,data)
    elif data > root.data:
        root.right = delete(root.right,data)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        temp = min_node(root.right)
        root.data = temp.data
        root.right = delete(root.right,temp.data)

    root.height = 1+max(height(root.left),height(root.right))
    bal = balance(root)

    if bal > 1 and data < root.left.data:
        return right_rotate(root)
    if bal < -1 and data > root.right.data:
        return left_rotate(root)
    if bal > 1 and data > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if bal < -1 and data < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root

    


root = None
 
root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 25)
 
"""The constructed AVL Tree would be
            30
           /  \
         20   40
        /  \     \
       10  25    50"""
 

preorder(root)
print()

root = delete(root, 20)

preorder(root)
print()