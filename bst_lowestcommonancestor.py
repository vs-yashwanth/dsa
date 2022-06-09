class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def lca(root,n1,n2):  # O(h) | O(log(n))
    if not root:
        return root
    if root.data < n1 and root.data < n2:
        return lca(root.right,n1,n2)
    elif root.data > n1 and root.data >n2 :
        return lca(root.left,n1,n2)
    else:
        return root

def lca_iter(root,n1,n2):
    if not root:
        return root
    q = [root]
    while q:
        temp = q.pop(0)
        if temp.data > n1 and temp.data >n2:
            q.append(temp.left)
        elif temp.data < n1 and temp.data < n2:
            q.append(temp.right)
        else:
            return temp
            break
    return root

def main():
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
      
    n1 = 10 ; n2 = 14
    t = lca(root, n1, n2)
    print ("LCA of %d and %d is %d" %(n1, n2, t.data))
    t = lca_iter(root, n1, n2)
    print ("-LCA of %d and %d is %d" %(n1, n2, t.data))
      
    n1 = 14 ; n2 = 8
    t = lca(root, n1, n2)
    print ("LCA of %d and %d is %d" %(n1, n2 , t.data))
    t = lca_iter(root, n1, n2)
    print ("-LCA of %d and %d is %d" %(n1, n2 , t.data))
      
    n1 = 10 ; n2 = 22
    t = lca(root, n1, n2)
    print ("LCA of %d and %d is %d" %(n1, n2, t.data))
    t = lca_iter(root, n1, n2)
    print ("-LCA of %d and %d is %d" %(n1, n2, t.data))


main()