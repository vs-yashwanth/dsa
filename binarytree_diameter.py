class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None

class Height:
    def __init__(self):
        self.h = 0

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameter(root):  # O(n^2)
    if not root:
        return 0
    
    lheight = height(root.left)
    rheight = height(root.right)
    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max ( (1+lheight+rheight), ldiameter,rdiameter)

def diameter_optim(root):

    height = Height()
    return diameter_aux(root,height)

def diameter_aux(root, height):
    if not root:
        return 0
    lh = Height()
    rh = Height()
    
    ldiameter = diameter_aux(root.left,lh)
    rdiameter = diameter_aux(root.right,rh)

    height.h = 1+ max(lh.h, rh.h)
    
    return max((1+lh.h+rh.h), ldiameter, rdiameter)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print(diameter(root))
print(diameter_optim(root))