class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def zigzag(root):
    now = []
    next = []
    now.append(root)
    order = True
    while now:
        temp=now.pop()
        print(temp.data,end=' ')
        if order:
            if temp.left:
                next.append(temp.left)
            if temp.right:
                next.append(temp.right)
        else:
            if temp.right:
                next.append(temp.right)
            if temp.left:
                next.append(temp.left)
        if not now:
            order = not order
            now,next = next,now

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)

zigzag(root)