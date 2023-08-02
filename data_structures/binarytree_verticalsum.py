from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def vertical_sum(root,hd,d):
    if not root:
        return 0
    d[hd] += root.data
    vertical_sum(root.left,hd-1,d)
    vertical_sum(root.right,hd+1,d)


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7)
d=defaultdict(int)
vertical_sum(root,0,d)
print(d.values())
