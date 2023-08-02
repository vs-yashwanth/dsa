class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def paths(root):
    path =[]
    helper(root,path)

def helper(root,path):

    path.append(root.data)
    if root.left:
        # left_path = path.copy()
        helper(root.left,path+[])
    if root.right:
        # right_path = path.copy()
        helper(root.right,path+[])
    if not root.left and not root.right:
        print(path)

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
paths(root)

