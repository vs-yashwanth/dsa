class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

maxi = 0
def paths(root):

    run = 0
    helper(root,0)
    
def helper(root,run):
    global maxi
    if not root:
        return 
    run += root.data
    if not root.left or root.right:
        maxi = max(run,maxi)
    helper(root.left,run)
    helper(root.right,run)
    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(2)

paths(root)
print(maxi)


