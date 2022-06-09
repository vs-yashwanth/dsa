class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.equal = None
        self.end = False

class TernarySearchTree:
    def __init__(self):
        self.root = Node('z')
    
    def insert(self,root,string,id):
        n = len(string)
        if id >= n:
            return root
        if not root:
            root =  Node(string[id])
            

        if string[id] < root.data:
            root.left = self.insert(root.left,string,id)
        elif string[id] > root.data:
            root.right = self.insert(root.right,string,id)
        else:
            if id < n:
                root.equal = self.insert(root.equal,string,id+1)
            if id+1 >= n:
                root.end = True
        return root
    
    def search(self,root,string,id):
        
        if not root or id >= len(string):
            return False
        if string[id] < root.data:
            return self.search(root.left,string,id)
        elif string[id] > root.data:
            return self.search(root.right,string,id)
        else:
            if id+1 >= len(string):
                return root.end
            return self.search(root.equal,string, id+1)
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data, end='')
            if root.end:
                print(', ',end='')
                
            self.inorder(root.equal)
            self.inorder(root.right)

if __name__ == '__main__':

    tst = TernarySearchTree()
    root = tst.root
    root = tst.insert(root,'cat',0)
    root = tst.insert(root,'dog',0)
    root = tst.insert(root,'pig',0)
    root = tst.insert(root,'birds',0)

    print('tst words: ')
    tst.inorder(root)
    print('\n')

    print(tst.search(root,'cat',0))
    print(tst.search(root,'boo',0))
    print(tst.search(root,'dog',0))
    print(tst.search(root,'pig',0))
    
