class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

pre = 0
def construct(preorder, inorder, in_s,in_e):
    global pre
    if in_s > in_e:
        return None

    temp = Node(preorder[pre])
    pre += 1
    if in_s == in_e:
        return temp
    in_i = inorder.index(temp.data)
    temp.left = construct(preorder,inorder,in_s,in_i-1)
    temp.right = construct(preorder,inorder,in_i+1,in_e)
    return temp

def show(root):
    if root:
        show(root.left)
        print(root.data,end=' ')
        show(root.right)

def main():
    preorder = [ 'A', 'B', 'D', 'E', 'C', 'F' ]
    inorder = [ 'D', 'B', 'E', 'A', 'F', 'C' ]
    root = construct(preorder,inorder,0,len(inorder)-1)
    show(root)

main()