class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def is_subtree(t,s):
    if not s:
        return True
    if not t:
        return False
    
    if identical(t,s):
        return True
    else:
        return is_subtree(t.left,s) or (t.right,s)

def identical(r1,r2):
    if r1 is r2:
        return True
    if not r1 or not r2:
        return False
    return ( r1.data == r2.data and
                identical(r1.left, r2.left) and
                    identical(r1.right, r2.right) )
                


T = Node(26)
T.right = Node(3)
T.right.right  = Node(3)
T.left = Node(10)
T.left.left = Node(4)
T.left.left.right = Node(30)
T.left.right = Node(6)
 
""" TREE 2
     Construct the following tree
          10
        /    \
      4      6
       \
        30
    """
S = Node(10)
S.right = Node(6)
S.left = Node(4)
S.left.right = Node(30)
 
if is_subtree(T, S):
    print ("Tree 2 is subtree of Tree 1")
else :
    print ("Tree 2 is not a subtree of Tree 1")
