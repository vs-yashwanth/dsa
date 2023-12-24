class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def max_level(root):
    q=[root]
    maxi=0
    max_sum = -float('inf')
    level=[]
    while q:
        temp=q.pop(0)
        if temp.left:
            level.append(temp.left)
        if temp.right:
            level.append(temp.right)
        if not q:
            q.extend(level)
            level = [i.data for i in level]
            maxi = max(maxi,len(level))
            max_sum = max(max_sum, sum(level))
            level =[]
    return maxi,max_sum

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print(max_level(root))