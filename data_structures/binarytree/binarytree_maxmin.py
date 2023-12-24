class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def stats(root):
    s = [root]
    elements = []
    while s:
        temp = s.pop()
        elements.append(temp.data)
        if temp.right:
            s.append(temp.right)
        if temp.left:
            s.append(temp.left)
    return max(elements), min(elements)

def max_recursive(root,maxi):
    if not root:
        return maxi
    max_left = max_right = maxi
    if root.left:
        max_left = max_recursive(root.left,maxi)
    if root.right:
        max_right = max_recursive(root.right,maxi)
    return max(maxi,max_left, max_right,root.data)

root=Node(10)
root.left=Node(11)
root.right=Node(9)
root.left.left=Node(7)
root.right.left=Node(15)
root.right.right=Node(8)

print(stats(root))
print(max_recursive(root,root.data))

