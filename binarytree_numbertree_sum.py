class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def paths(root):
    path = 0
    paths=[0]
    helper(root,path,paths)
    print(paths[0])

def helper(root,path,paths):

    path= path*10 + (root.data)
    if root.left:
        helper(root.left,path,paths)
    if root.right:
        helper(root.right,path,paths)
    if not root.left and not root.right:

        paths[0] += path

root = Node(1)
root.left = Node(2)
root.right = Node(3)

paths(root)


