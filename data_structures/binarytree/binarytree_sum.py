class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def tree_sum(root):
    if not root:
        return 0
    return root.data+tree_sum(root.left)+tree_sum(root.right)

def tree_sum_iter(root):

    run = 0
    q=[root]
    while q:
        temp = q.pop(0)
        run += temp.data
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    return run


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(2)
root.left.right = Node(2)

print(tree_sum(root))
print(tree_sum_iter(root))




