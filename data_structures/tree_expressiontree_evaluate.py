class node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

def evaluate(root):
    if not root:
        return 0

    if not root.left or not root.right:
        return root.data
    
    left = str(evaluate(root.left))
    right = str(evaluate(root.right))
    return eval(left+root.data+right)

def main():
    root = node('+')
    root.left = node('*')
    root.left.left = node('5')
    root.left.right = node('-4')
    root.right = node('-')
    root.right.left = node('100')
    root.right.right = node('20')

    print(evaluate(root))

    root = None
    root = node('+')
    root.left = node('*')
    root.left.left = node('5')
    root.left.right = node('4')
    root.right = node('-')
    root.right.left = node('100')
    root.right.right = node('/')
    root.right.right.left = node('20')
    root.right.right.right = node('2')
    print (evaluate(root))
main()