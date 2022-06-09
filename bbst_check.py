class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

class Height:
    def __init__(self):
        self.h = 0
    
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left),height(root.right))

def check(root): # O(n**2)
    if not root:
        return True
    left = height(root.left)
    right = height(root.right)
    if (abs(left-right) <= 1 
        and check(root.left) 
            and check(root.right)):
        return True
    return False

def check2(root,height):  # O(n)
    if not root:
        return True
    lh = Height()
    rh = Height()
    left = check2(root.left,lh)
    right = check2(root.right,rh)
    height.h = 1 + max(lh.h, rh.h)
    
    return abs(lh.h - rh.h) <= 1 and left and right



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
print(check(root))
print(check2(root,Height()))
