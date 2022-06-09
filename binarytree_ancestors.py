class Node:
    def __init__(self,data):
        self.data = data
        self.prev = self.next = None

def ancestors(root,key):
    if not root:
        return root
    if root.data == key:
        return True

    if ancestors(root.left,key) or ancestors(root.right,key):
        print(root.data)
        return True
    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
  
ancestors(root, 7)
  

