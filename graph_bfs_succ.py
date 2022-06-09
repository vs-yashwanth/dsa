# not working
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def insert(root,data):
    if not root:
        return Node(data)
    if root.data == data:
        return root
    if root.data < data:
        root.right = insert(root.right,data)
    if root.data > data:
        root.left = insert(root.left,data)

def succ(root):
    if not root or not root.right:
        return root
    root = root.right
    while root.left:
        root = root.left
    return root

def find(root,key):
    if not root:
        return root
    if root.left.data == key:
        return succ(root.left)
    if root.right.data == key:
        return succ(root.right)    
    elif root.data < key:
        return find(root.right,key)
    else:
        return find(root.left,key)

def main():
    root = None
 
    # Creating the tree given in the above diagram
    root = insert(root, 20)
    root = insert(root, 8);
    root = insert(root, 22);
    root = insert(root, 4);
    root = insert(root, 12);
    root = insert(root, 10); 
    root = insert(root, 14);   
     
    succ = find( root, 8)
    if succ is not None:
        print ("\nInorder Successor of 14 is % d "  %(succ.data))
    else:
        print ("\nInorder Successor doesn't exist")
main()