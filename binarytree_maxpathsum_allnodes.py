class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

maxi = -float('inf')

def max_path_sum(root):
    global maxi
    if not root:
        return 0

    left = max_path_sum(root.left)
    right = max_path_sum(root.right)

    max_here = max(max(left,right)+root.data, root.data)
    max_top = max(max_here, left+right+root.data)

    maxi = max(maxi, max_top)

    return max_here

root = Node(10)
root.left = Node(2)
root.right   = Node(10);
root.left.left  = Node(20);
root.left.right = Node(1);
root.right.right = Node(-25);
root.right.right.left   = Node(3);
root.right.right.right  = Node(4);
max_path_sum(root)
print(maxi)

