class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def insert(root,data):
    if not root:
        return Node(data)
    if root.data==data:
        return root
    if root.data < data:
        root.right = insert(root.right,data)
    else:
        root.left = insert(root.left,data)
    return root

def min_node(root):
    if not root:
        return root
    while root.left:
        root = root.left
    return root

def successor(root,node):
    if not root:
        return root
    if node.right:
        return min_node(node.right)
    while root:
        if root.data < node.data:
            root = root.right
        elif root.data>node.data:
            succ = root
            root = root.left
        else:
            break
    return succ
if __name__ == '__main__':
    root = None
    root = insert(root, 20)
    root = insert(root, 8);
    root = insert(root, 22);
    root = insert(root, 4);
    root = insert(root, 12);
    root = insert(root, 10); 
    root = insert(root, 14);   
    temp = root.left.right.right

    print(temp.data,'->',successor(root,temp).data)
