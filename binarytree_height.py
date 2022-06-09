class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if not root:
        return -1
    return 1+max(height(root.left),height(root.right))

def height_iter(root):
    q= [root]
    aux = []
    count = -1
    while q:
        temp = q.pop(0)

        if temp.left:
            aux.append(temp.left)
        if temp.right:
            aux.append(temp.right)
        if not q:
            count += 1
            q.extend(aux)
            aux = []
    return count

def karumanchi(root):
    q = [(root,0)]
    while q:
        temp, maxi = q.pop(0)
        if temp.left:
            q.append((temp.left,maxi+1))
        if temp.right:
            q.append((temp.right,maxi+1))
    return maxi


root=Node(10)
root.left=Node(11)
root.right=Node(9)
root.left.left=Node(7)
root.right.left=Node(15)
root.right.right=Node(8)

print(height_iter(root))
print(height(root))
print(karumanchi(root))