class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	

def inorder_stack(root):
    S=[]
    current=root
    while S or current:
        if current:
            S.append(current)
            current=current.left
        if not current:
            temp=S.pop()
            print(temp.data,end=' ')
            current=temp.right



root=Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)


inorder_stack(root)

 