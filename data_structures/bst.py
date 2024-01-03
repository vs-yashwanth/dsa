from binarytree import BinaryTree
from queue_py import QueueRaw


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# time complexity: O(log n) if tree is balanced else O(n)


class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if not root:
            node = Node(val)
            if not self.root:
                self.root = node
            return node

        if root.val == val:
            return
        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def insert_iter(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
            return
        cur = self.root
        while cur:
            if val == cur.val:
                return
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    break
            elif val > cur.val:
                if cur.right:
                    cur = cur.right
                else:
                    break

        if val < cur.val:
            cur.left = node
        else:
            cur.right = node
        return

    def search(self, root, target):
        if not root:
            return False
        if root.val == target:
            return True
        if target < root.val:
            return self.search(root.left, target)
        else:
            return self.search(root.right, target)

    def delete(self, root, target):
        if not root:
            return root
        if root.val == target:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                inorder_predecessor = self.max_node(root.left)
                root.val = inorder_predecessor
                root.left = self.delete(root.left, inorder_predecessor)
        elif target < root.val:
            root.left = self.delete(root.left, target)
        else:
            root.right = self.delete(root.right, target)

        return root

    def minimum(self):
        cur = self.root
        if not cur:
            return 0
        while cur.left:
            cur = cur.left
        return cur.val

    def maximum(self):
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur.val

    def min_node(self, root):

        while root.left:
            root = root.left
        return root.val

    def max_node(self, root):

        while root.right:
            root = root.right
        return root.val

    def size(self, root):
        if not root:
            return 0
        return self.size(root.left) + 1 + self.size(root.right)


if __name__ == '__main__':

    bst = BinarySearchTree()

    # Test case 1: Insert single node
    bst.insert(bst.root, 50)
    # Expected output: 50
    print("Inorder traversal (single node):")
    print(bst.inorder(bst.root))

    # Test case 2: Insert duplicate node
    bst.insert(bst.root, 50)
    # Expected output: 50 50
    print("Inorder traversal (duplicate nodes):")
    print(bst.inorder(bst.root))

    # Test case 3: Insert nodes in a zigzag pattern
    bst = BinarySearchTree()
    bst.insert(bst.root, 50)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 70)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 40)
    bst.insert(bst.root, 60)
    bst.insert(bst.root, 80)
    # Expected output: 20 30 40 50 60 70 80
    print("Inorder traversal (zigzag pattern):")
    print(bst.inorder(bst.root))

    print('Deletion')
    # Test case 4: Delete a leaf node
    bst.delete(bst.root, 20)
    # Expected output: 30 40 50 60 70 80
    print(bst.inorder(bst.root))

    # Test case 5: Delete a node with one child
    bst.delete(bst.root, 30)
    # Expected output: 40 50 60 70 80
    print(bst.inorder(bst.root))

    # Test case 6: Delete a node with two children
    bst.delete(bst.root, 50)
    # Expected output: 40 60 70 80
    print(bst.inorder(bst.root))

    # Test case 7: Find minimum and maximum values in an empty tree
    min_val = bst.minimum()
    max_val = bst.maximum()
    # Expected output: Minimum: 40, Maximum: 80
    print(f"Minimum {min_val}, Maximum {max_val}")

    # Test case 8: Search for a node that doesn't exist
    search_result_nonexistent = bst.search(bst.root, 10)
    # Expected output: Key not found
    print(search_result_nonexistent)

    # Test case 9: Search for a node that exists
    search_result_existing = bst.search(bst.root, 60)
    # Expected output: 60
    print(search_result_existing)

    # Test case 10: Size of tree
    print(bst.size(bst.root))
    # expected: 4

    print(bst.levels())
