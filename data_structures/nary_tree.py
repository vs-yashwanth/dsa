class Node:
    def __init__(self,data):
        self.data=data
        self.left = self.right = None
def is_op(x):
    ops = {'+','-','*','/','%','^'}
    return x in ops

def build(postfix):
    s = []
    for i in postfix:
        if is_op(i):

            a = s.pop()
            b = s.pop()
            temp = Node(i)
            temp.right = a
            temp.left = b
            s.append(temp)            
        else:
            temp = Node(i)
            s.append(temp)
    return s.pop()

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)


def main():
    postfix = "ab+ef*g*-"
    root = build(postfix)
    inorder(root)
main()
