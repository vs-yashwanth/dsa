class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def convert(A,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    root = Node(A[mid])
    root.left = convert(A,start,mid-1)
    root.right = convert(A,mid+1,end)
    return root

def preorder(root):
    if root:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)

arr =[-10,-3,0,5,9]
root = convert(arr,0,len(arr)-1)
preorder(root)