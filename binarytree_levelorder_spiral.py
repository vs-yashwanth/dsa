class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        

class Tree:
    def __init__(self):
        self.root = None
    
    def levelorder_rev(self):
        temp = self.root
        q = [temp]
        next = []
        out = [temp]
        flag = True
        while q:
            temp = q.pop(0)
            if temp.left:
                next.append(temp.left)
            if temp.right:
                next.append(temp.right)
            if not q:
                q = next.copy()
                if flag:
                    out += next
                else:
                    out += next[::-1]
                next = []
                flag = not flag
        print([i.data for i in out])


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)

    T = Tree()
    T.root = root
    T.levelorder_rev()