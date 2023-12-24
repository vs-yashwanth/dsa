from queue_py import QueueRaw
from stack import StackRaw, StackArray


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def preorder(self, root, out=None):
        if out is None:
            out = []
        if root:
            out.append(root.val)
            self.preorder(root.left, out)
            self.preorder(root.right, out)
            return out

    def inorder(self, root, out=None):
        if out is None:
            out = []
        if root:
            self.inorder(root.left, out)
            out.append(root.val)
            self.inorder(root.right, out)
            return out

    def postorder(self, root, out=None):
        if out is None:
            out = []
        if root:
            self.postorder(root.left, out)
            self.postorder(root.right, out)
            out.append(root.val)
            return out

    def preorder_iter(self):
        if not self.root:
            return
        root = self.root
        stack = StackRaw()
        stack.push(root)
        out = []
        while not stack.is_empty():
            cur = stack.pop()
            out.append(cur.val)
            if cur.right:
                stack.push(cur.right)
            if cur.left:
                stack.push(cur.left)
        return out

    def inorder_iter(self):
        root = self.root
        out = []
        if not root:
            return out
        stack = StackRaw()
        cur = root
        while not stack.is_empty() or cur:
            if cur:
                stack.push(cur)
                cur = cur.left

            else:
                cur = stack.pop()
                out.append(cur.val)
                cur = cur.right
        return out

    def postorder_iter_1(self):
        root = self.root
        out = []
        if not root:
            return out
        stack1 = StackRaw()
        stack2 = StackRaw()
        stack1.push(root)
        while not stack1.is_empty():
            cur = stack1.pop()
            stack2.push(cur)
            if cur.left:
                stack1.push(cur.left)
            if cur.right:
                stack1.push(cur.right)
        while not stack2.is_empty():
            out.append(stack2.pop().val)
        return out

    def postorder_iter_2(self):
        root = self.root
        out = []
        if not root:
            return out
        stack = StackRaw()
        visited = set()
        cur = root
        while not stack.is_empty() or cur:
            if cur:
                stack.push(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if cur.right and cur.right not in visited:
                    stack.push(cur)
                    cur = cur.right
                else:
                    visited.add(cur)
                    out.append(cur.val)
                    cur = None
        return out

    def levelorder(self):
        root = self.root
        out = []
        queue = QueueRaw()
        queue.enqueue(root)
        while not queue.is_empty():
            temp = queue.dequeue()
            out.append(temp.val)
            if temp.left:
                queue.enqueue(temp.left)
            if temp.right:
                queue.enqueue(temp.right)
        return out

    def levels(self):
        root = self.root
        out = [[root.val]]
        queue = QueueRaw()
        queue.enqueue(root)
        level = []
        while not queue.is_empty():
            temp = queue.dequeue()
            if temp.left:
                level.append(temp.left)
            if temp.right:
                level.append(temp.right)
            if queue.is_empty() and level:
                out.append([i.val for i in level])
                for i in level:
                    queue.enqueue(i)
                level = []
        return out

    def height_recursive(self, root):
        if not root:
            return -1
        else:
            return 1 + max(self.height_recursive(root.left), self.height_recursive(root.right))

    def height(self):
        root = self.root
        if not root:
            return 0
        queue = QueueRaw()
        aux = []
        count = 0
        queue.enqueue(root)
        while not queue.is_empty():
            cur = queue.dequeue()
            if cur.left:
                aux.append(cur.left)
            if cur.right:
                aux.append(cur.right)
            if queue.is_empty():
                count += 1
                for i in aux:
                    queue.enqueue(i)
                aux = []
        return count - 1

    def insert(self, val):
        root = self.root
        node = TreeNode(val)
        if not root:
            self.root = node
            return
        queue = QueueRaw()
        queue.enqueue(root)
        while not queue.is_empty():
            cur = queue.dequeue()
            if cur.left:
                queue.enqueue(cur.left)
            else:
                cur.left = node
                return
            if cur.right:
                queue.enqueue(cur.right)
            else:
                cur.right = node
                return

    def delete(self, val):
        root = self.root
        if not root:
            return
        if not root.left and not root.right:
            if root.val == val:
                self.root = None
                return
            else:
                return

        target = None
        cur = None
        prev = None
        queue = QueueRaw()
        queue.enqueue(root)
        while not queue.is_empty():
            cur = queue.dequeue()
            if cur.val == val:
                target = cur
            if cur.left:
                prev = cur
                queue.enqueue(cur.left)
            if cur.right:
                prev = cur
                queue.enqueue(cur.right)

        if target:
            target.val = cur.val
            if prev.left is cur:
                prev.left = None
            else:
                prev.right = None

    def search(self, val):
        root = self.root
        if not root:
            return False
        queue = QueueRaw()
        queue.enqueue(root)
        while not queue.is_empty():
            cur = queue.dequeue()
            if cur.val == val:
                return True
            if cur.left:
                queue.enqueue(cur.left)
            if cur.right:
                queue.enqueue(cur.right)
        return False

    def search_recursive(self, root, val):
        if not root:
            return False
        if root.val == val:
            return True
        return self.search_recursive(root.left, val) or self.search_recursive(root.right, val)

    def size(self):
        root = self.root
        if not root:
            return 0
        count = 0
        queue = QueueRaw()
        queue.enqueue(root)
        while not queue.is_empty():
            cur = queue.dequeue()
            count += 1
            if cur.left:
                queue.enqueue(cur.left)
            if cur.right:
                queue.enqueue(cur.right)
        return count

    def size_recursive(self, root):
        if not root:
            return 0
        return 1 + self.size_recursive(root.left) + self.size_recursive(root.right)

    def sum(self):
        root = self.root
        if not root:
            return 0
        total = 0
        queue = QueueRaw()
        queue.enqueue(root)
        while not queue.is_empty():
            cur = queue.dequeue()
            total += cur.val
            if cur.left:
                queue.enqueue(cur.left)
            if cur.right:
                queue.enqueue(cur.right)
        return total

    def sum_recursive(self, root):
        if not root:
            return 0
        return root.val + self.sum_recursive(root.left) + self.sum_recursive(root.right)


if __name__ == '__main__':

    # Tree structure:
    #        5
    #       / \
    #      3   8
    #     / \   \
    #    2   4   10
    #   /       / \
    #  1       9   12

    tree = BinaryTree()
    tree.root = TreeNode(5)
    tree.root.left = TreeNode(3)
    tree.root.right = TreeNode(8)
    tree.root.left.left = TreeNode(2)
    tree.root.left.right = TreeNode(4)
    tree.root.left.left.left = TreeNode(1)
    tree.root.right.right = TreeNode(10)
    tree.root.right.right.left = TreeNode(9)
    tree.root.right.right.right = TreeNode(12)

    # Run the test cases using methods of BinaryTree class
    print("In-Order Traversal:")
    print(tree.inorder(tree.root))
    print(tree.inorder_iter())
    print()

    print("Pre-Order Traversal:")
    print(tree.preorder(tree.root))  # Expected Output: 5 3 2 1 4 8 10 9 12
    print(tree.preorder_iter())
    print()

    print("Post-Order Traversal:")
    print(tree.postorder(tree.root))  # Expected Output: 1 2 4 3 9 12 10 8 5
    print(tree.postorder_iter_1())
    print(tree.postorder_iter_2())
    print()

    print('Level order traversal')
    print(tree.levelorder())  # Expected Output: 5 3 8 2 4 10 1 9 12
    print()

    print('Height')
    print(tree.height_recursive(tree.root))
    print(tree.height())
    print()

    print('Inserting')
    print(tree.inorder(tree.root))  # Expected Output: 1 2 3 4 5 8 9 10 12
    tree.insert(11)
    print(tree.inorder(tree.root))
    print()

    print('Deletion')
    print(tree.inorder(tree.root))
    tree.delete(11)
    print(tree.inorder(tree.root))
    print()

    print('Searching')
    print(tree.search(9), tree.search(20))
    print(tree.search_recursive(tree.root, 9),
          tree.search_recursive(tree.root, 20))
    # expected: True False
    print()

    print('Size')
    print(tree.size())   # expected: 9
    print(tree.size_recursive(tree.root))   # expected: 9
    print()

    print('Sum')
    print(tree.sum())
    print(tree.sum_recursive(tree.root))
