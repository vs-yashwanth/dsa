class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# if we have to maintain a single pointer, then only
# tail can be maintained and head can be obtained as its next

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        out = ''
        cur = self.head
        while cur:
            out += f'{cur.val} '
            cur = cur.next
            if cur is self.head:
                break
        return out
    
    def traverse(self):
        s= []
        cur = self.head
        while cur:
            if cur.val in s:
                print('culprit', cur.val)
                print(s)
                break
            s.append(cur.val)
            print(cur.val, end=' ')
            cur = cur.next
            if cur is self.head:
                break
        print()
    
    def push(self, val):
        node = Node(val)
        cur = self.head
        if not cur:
            node.next = node
            self.head = node
            self.tail = node
            return
        while cur.next is not self.head:
            cur = cur.next
        node.next = self.head
        cur.next = node
        self.tail = node

    def pushLeft(self, val):
        node = Node(val)
        cur = self.head
        if not cur:
            node.next = node
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.next = self.head
        self.head = node
    
    def length(self):
        cur = self.head
        if not cur: return 0
        count = 0
        while True:
            count += 1
            cur = cur.next
            if cur is self.head:
                break
        return count
    
    def insert(self,ind, val):
        node = Node(val)
        cur = self.head
        length = self.length()
        if ind > length: return
        elif ind == length: 
            self.push(val)
            return
        elif ind == 0:
            self.pushLeft(val)
            return
        
        for _ in range(ind-1):
            cur = cur.next
        node.next = cur.next
        cur.next = node

    def pop(self):
        cur = self.head
        if not cur: return
        while cur.next is not self.tail:
            cur = cur.next
        cur.next = self.head
        out = self.tail
        self.tail = cur
        return out.val
    
    def popLeft(self):
        out = self.head
        self.tail.next = self.head.next
        self.head = self.head.next
        return out.val
   
    def remove(self, val):
        cur = self.head
        if cur.val == val:
            self.popLeft()
            return
        while cur:
            if cur.next.val == val:
                cur.next = cur.next.next
                return 
            cur = cur.next
            if cur is self.head:
                break


    def removeAt(self, ind):
        cur = self.head
        length = self.length()
        if ind >= length: return
        if ind == length -1 : 
            self.pop()
            return
        elif ind == 0:
            self.popLeft()
            return

        for _ in range(ind-1):
            cur = cur.next
            if cur is self.head:
                return
        
        cur.next = cur.next.next


    def fromEnd(self, ind): 
        length = self.length()
        if ind >= length: return None
        slow = self.head
        fast = self.head
        for _ in range(ind):
            fast = fast.next
            if fast is self.head:
                break
        while fast.next is not self.head:
            slow = slow.next
            fast = fast.next
        return slow.val

    
    def middle(self):
        slow = self.head
        fast = self.head
        while True:
            fast = fast.next
            if fast is self.head or fast.next is self.head:
                break
            slow = slow.next
            fast = fast.next
        return slow.val
    
    def reversePrint(self, node):
        if node.next is self.head:
            print(node.val, end=' ')
            return
        self.reversePrint(node.next)
        print(node.val, end=' ')
        if node is self.head:
            print()

    def reverse(self): 
        cur = self.head
        prev = self.head
        while prev:
            if prev.next is self.head:
                break
            prev = prev.next
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            if cur is self.head:
                break
        self.head = prev

    def reverseRecursive(self, node):
        if node.next is self.head:
            self.head = node
            return
        self.reverseRecursive(node.next)
        node.next.next = node
        node.next = self.head

    def sum(self): 
        count = 0
        cur = self.head
        while cur:
            if type(cur.val) is not int and type(cur.val) is not float:
                return None
            count += cur.val
            cur = cur.next
            if cur is self.head:
                break
        return count
    
    def sumRecursive(self, node): 
        if node.next is self.head:
            return node.val
        return node.val + self.sumRecursive(node.next)
    
    def show(self):
        cur = self.head
        while cur:
            print(cur.val, end=' ')
            cur = cur.next
            if cur is self.head:
                break
        print()
        

    def isALoop(self):

        slow = self.head
        fast = self.head
        while fast:
            fast = fast.next
            if fast is self.head or fast.next is self.head:
                return True
            fast = fast.next
            slow = slow.next
            if slow is fast:
                return True
        return False
    
    def loopStart(self):

        # works because meeting place to starting point will be 
        # the same distance as head to starting point

        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                slow = self.head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow.val
        return None
    
    def loopLength(self):

        slow = self.head
        fast = self.head
        while fast:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                count = 0
                while True:
                    count += 1
                    slow = slow.next
                    if slow is fast:
                        break
                return count
        return None
    
    def sortedInsert(self, val):
        node = Node(val)
        cur = self.head
        if not cur:
            self.push(val)
            return 
        
        if cur.val >= val:
            self.pushLeft(val)
            return
        
        while cur and cur.next:
            if cur.next is self.head:
                break
            if cur.val < val <= cur.next.val:
                node.next = cur.next
                cur.next = node
                return
            cur = cur.next
        self.push(val)
        return
    
    def reverseInPairs(self):
        cur = self.head
        if not cur: return
        nxt = cur.next
        prev = cur
        while prev.next is not self.head:
            prev = prev.next
        while True:
            cur.next = nxt.next
            nxt.next = cur
            if prev.next is self.head: self.head = nxt
            prev.next = nxt

            prev = cur
            cur = cur.next
            nxt = cur.next

            if cur is self.head or nxt is self.head: return
    
    def splitIntoTwo(self):
        slow = self.head
        if not slow: return
        prev = None
        fast = self.head
        while True:
            if fast.next is self.head or fast.next.next is self.head:
                break
            prev = slow
            fast = fast.next.next
            slow = slow.next
        
        if fast.next.next is self.head:
            prev = slow
            slow = slow.next
            fast.next.next = None
        elif fast.next is self.head:
            prev = slow
            slow = slow.next
            fast.next = None
        if prev: prev.next = None

        return self.head, slow
    
    def traverseFrom(self,node):
        s = []
        while node:
            print(node.val, end=' ')
            node = node.next
        print()

    def end_node(self):
        cur = self.head
        if not cur: return cur
        while cur.next is not self.head:
            cur = cur.next
        return cur


    def isPalindrome(self):
        cur = self.head
        if not cur: return False
        if not cur.next: return True
        slow = cur
        fast = cur
        while fast.next is not self.head and fast.next.next is not self.head:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        mid = mid.next
        stack = []
        while mid is not self.head:
            stack.append(mid.val)
            mid = mid.next
        while stack:
            out = stack.pop()
            if out != cur.val:
                return False
            cur = cur.next
        return True
    
    def reverse_k(self, k):
        head = self.head
        if k <= 1 or not head or head.next == head:
            return head
    
        # Count the total number of nodes in the circular linked list
        total_nodes = 1
        current = head
        while current.next != head:
            current = current.next
            total_nodes += 1
        
        # Adjust k in case it's greater than the total number of nodes
        k = min(k, total_nodes)
        
        dummy = Node(0)
        dummy.next = head
        prev_group_end = dummy
        
        while total_nodes >= k:
            current_group_start = prev_group_end.next
            current = current_group_start
            prev = None
            count = 0
            
            while count < k:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                count += 1
            
            prev_group_end.next.next = current
            prev_group_end.next = prev
            
            prev_group_end = current_group_start
            total_nodes -= k
        
        return dummy.next

    def reverse_k_recursive(self, head, k):
        if not head: return head
        cur = head
        prev = None
        count = 0
        while count < k:
            nxt = cur.next
            cur.next = prev if cur.next is not self.head else self.head
            prev = cur
            cur = nxt
            if cur is self.head: break
            count += 1
        if nxt is not self.head:
            rev = self.reverse_k_recursive(nxt, k)
            head.next = rev

        if head is self.head:
            end_node = self.end_node()
            if end_node: 
                end_node.next = prev
            self.head = prev
        return prev

    def sortedRemoveDuplicates(self):
        cur = self.head
        if not cur: return cur
        while True:
            nxt = cur.next
            while nxt is not self.head and cur.val == nxt.val:
                cur.next = nxt.next
                nxt = nxt.next
            cur = cur.next
            if cur is self.head: break

    def seperateEvenOdd(self):
        cur = self.head
        if not cur: return cur
        prev = None
        evenLL = CircularLinkedList()
        while True:
            if cur.val % 2 == 0:
                evenLL.push(cur.val)
                self.remove(cur.val)
            prev = cur
            cur = cur.next
            if cur is self.head:
                break
        prev.next = evenLL.head
        evenLL.end_node().next = self.head

if __name__ == '__main__':

    # Tests from ChatGPT :)

    linked_list = CircularLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(4)
    print(linked_list.isALoop())

    # Test 2: Display the linked list using '__str__'
    # Expected output: "1 -> 2 -> 3 -> 4"
    print(linked_list)

    # Test 3: Push elements to the left of the linked list using 'pushLeft'
    linked_list.pushLeft(5)
    linked_list.pushLeft(6)

    # Test 4: Display the linked list after 'pushLeft'
    # Expected output: "6 -> 5 -> 1 -> 2 -> 3 -> 4"
    print(linked_list)

    # Test 5: Insert an element at a specified index using 'insert'
    linked_list.insert(2, 10)
    linked_list.insert(4, 20)

    # Test 6: Display the linked list after 'insert'
    # Expected output: "6 -> 5 -> 10 -> 1 -> 20 -> 2 -> 3 -> 4"
    print(linked_list)

    # Test 7: Insert an element at the beginning of the linked list using 'insert'
    linked_list.insert(0, 100)

    # Test 8: Display the linked list after inserting at the beginning
    # Expected output: "100 -> 6 -> 5 -> 10 -> 1 -> 20 -> 2 -> 3 -> 4"
    print(linked_list)

    # Test 9: Insert an element at the end of the linked list using 'insert'
    linked_list.insert(linked_list.length(), 200)

    # Test 10: Display the linked list after inserting at the end
    # Expected output: "100 -> 6 -> 5 -> 10 -> 1 -> 20 -> 2 -> 3 -> 4 -> 200"
    print(linked_list)

    # Test 11: Pop an element from the end of the linked list using 'pop'
    popped_value = linked_list.pop()
    # Expected output: popped_value = 200, linked_list = "100 -> 6 -> 5 -> 10 -> 1 -> 20 -> 2 -> 3 -> 4"
    print(f"pop = {popped_value}, {linked_list}")

    # Test 12: Pop an element from the beginning of the linked list using 'popLeft'
    popped_value = linked_list.popLeft()
    # Expected output: popped_value = 100, linked_list = "6 -> 5 -> 10 -> 1 -> 20 -> 2 -> 3 -> 4"
    print(f"popLeft = {popped_value}, {linked_list}")

    # Test 13: Remove an element from the linked list using 'remove'
    linked_list.remove(10)
    # Expected output: linked_list = "6 -> 5 -> 1 -> 20 -> 2 -> 3 -> 4"
    print(linked_list)

    # Test 14: Try to remove an element that does not exist in the linked list using 'remove'
    try:
        linked_list.remove(1000)
    except ValueError as e:
        # Expected output: ValueError: Element 1000 not found in the list
        print(f"Error: {e}")

    # Test 15: Remove an element at a specified index using 'removeAt'
    linked_list.removeAt(0)
    # Expected output: "5 -> 1 -> 20 -> 2 -> 3 -> 4"
    print(linked_list)

    linked_list.removeAt(2)
    # Expected output: "5 -> 1 -> 2 -> 3 -> 4"
    print(linked_list)

    linked_list.removeAt(linked_list.length() - 1)
    # Expected output: "5 -> 1 -> 2 -> 3"
    print(linked_list)

    # Test 16: Display the linked list after 'removeAt'
    # Expected output: Varies depending on the removed indexes in Test 15
    print(linked_list)

    # Test 17: Try to remove an element at an invalid index using 'removeAt'
    try:
        linked_list.removeAt(linked_list.length())
    except ValueError as e:
        # Expected output: ValueError: Index out of range
        print(f"Error: {e}")

    # Test 18: Access an element from the end using 'fromEnd'
    value_from_end = linked_list.fromEnd(2)
    # Expected output: value_from_end = 3
    print(f"value_from_end = {value_from_end}")

    # Test 19: Try to access an element from an invalid index using 'fromEnd'
    try:
        linked_list.fromEnd(10)
    except IndexError as e:
        # Expected output: IndexError: Index out of range
        print(f"Error: {e}")

    # Test 20: Access the first element from the end using 'fromEnd'
    value_from_end = linked_list.fromEnd(0)
    # Expected output: value_from_end = 3
    print(f"value_from_end = {value_from_end}")

    # Test 21: Access the last element using 'fromEnd'
    value_from_end = linked_list.fromEnd(linked_list.length() - 1)
    # Expected output: value_from_end = 2
    print(f"value_from_end = {value_from_end}")
    
    # Test 22: Print the linked list in reverse order using 'reversePrint'
    linked_list.reversePrint(linked_list.head)
    # Expected output: "3 -> 2 -> 1 -> 5 -> "
    
    # Test 23: Get the middle element using 'middle'
    middle_value = linked_list.middle()
    # Expected output: middle_value = 1
    print(f"middle_value = {middle_value}")

    # Test 24: Create a new linked list with a single element and get its middle
    linked_list_single_element = CircularLinkedList()
    linked_list_single_element.push(99)
    middle_value_single_element = linked_list_single_element.middle()
    # Expected output: middle_value_single_element = 99
    print(f"middle_value_single_element = {middle_value_single_element}")

    # Test 25: Get the middle element from the modified linked list
    middle_value_modified = linked_list.middle()
    # Expected output: middle_value_modified = 2
    print(f"middle_value_modified = {middle_value_modified}")

    # Test 26: Create a new linked list with multiple elements and get its middle
    linked_list_multiple_elements = CircularLinkedList()
    linked_list_multiple_elements.push(11)
    linked_list_multiple_elements.push(22)
    linked_list_multiple_elements.push(33)
    middle_value_multiple_elements = linked_list_multiple_elements.middle()
    # Expected output: middle_value_multiple_elements = 22
    print(f"middle_value_multiple_elements = {middle_value_multiple_elements}")

    # Test 27: Reverse the linked list using 'reverse'
    linked_list.reverse()
    # Expected output: "3 -> 2 -> 1 -> 5"
    print(linked_list)

    # Test 28: Reverse the linked list using 'reverseRecursive'
    linked_list.reverseRecursive(linked_list.head)
    # Expected output: "5 -> 1 -> 2 -> 3"
    print(linked_list)

    # Test 29: Calculate the sum of the linked list using 'sum'
    linked_list.push(6.5)
    linked_list.push(8.2)
    linked_list.push(9)
    linked_list.push(4.7)
    linked_list.push(3)
    linked_list.push(2)

    total_sum = linked_list.sum()
    # Expected output: total_sum = 42.4 (sum of 5 + 1 + 2 + 3 + 6.5 + 8.2 + 9 + 4.7 + 3 + 2)
    print(f"total_sum = {total_sum}")

    # Test 30: Try to calculate the sum when the list contains non-number values
    try:
        invalid_linked_list = CircularLinkedList()
        invalid_linked_list.push(1)
        invalid_linked_list.push(2)
        invalid_linked_list.push("hello")
        invalid_linked_list.push(3)
        invalid_linked_list.push(4)

        total_sum = invalid_linked_list.sum()
        print(f"total_sum = {total_sum}")
    except ValueError as e:
        # Expected output: ValueError: All values in the list must be numbers
        print(f"Error: {e}")


    # Test 31: Calculate the sum of the linked list using 'sumRecursive'
    linked_list = CircularLinkedList()
    linked_list.push(6.5)
    linked_list.push(8.2)
    linked_list.push(9)
    linked_list.push(4.7)
    linked_list.push(3)
    linked_list.push(2)

    total_sum_recursive = linked_list.sumRecursive(linked_list.head)
    # Expected output: total_sum_recursive = 33.4 (sum of 5 + 1 + 2 + 3 + 6.5 + 8.2 + 9 + 4.7 + 3 + 2)
    print(f"total_sum_recursive = {total_sum_recursive}")
    print(linked_list)


    # Test 32: Check if the linked list has a loop using 'isALoop'
    print(linked_list.isALoop())
    # Expected output: True 

    # Test 33: Print the starting point of the loop using 'loopStart'
    print(linked_list.loopStart())
    # Expected output: 6.5

    # Test 34: Create a loop in the linked list and check again
    linked_list.head.next.next.next.next.next.next = linked_list.head.next
    print(linked_list.isALoop())
    # Expected output: False 

    # Test 35: Count the length of the loop using 'loopLength'
    print(linked_list.loopLength())
    # Expected output: 5

    # Test 36: Insert values into the correct place of a sorted array
    linked_list.sortedInsert(8.5)
    linked_list.sortedInsert(7)
    linked_list.sortedInsert(0)
    print(linked_list)
    # Expected output: 0 6.5 7 8.2 8.5 9 4.7 3 2

    # Test 37 - Reverse in pairs
    linked_list = CircularLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(4)
    linked_list.push(5)
    linked_list.push(6)
    linked_list.reverseInPairs()
    print(linked_list)
    # Expected output: 2 1 4 3 6 5

    # Test 38 - Split into two 
    one, two = linked_list.splitIntoTwo()
    linked_list.traverseFrom(one)
    linked_list.traverseFrom(two)
    # Expected output: 2 1 4 , 3 6 5


    # Test 39 - check if linked list is a palindrome
    linked_list = CircularLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(4)
    print(linked_list.isPalindrome())
    # Expected output: False

    # Test 40 - check if linked list is a palindrome
    linked_list = CircularLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(4)
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    print(linked_list.isPalindrome())
    # Expected output: True

    # Test 41 - reverse in groups
    linked_list = CircularLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(4)
    linked_list.push(5)
    linked_list.push(6)
    #linked_list.reverse_k(3)
    #print(linked_list)
    # Expected output: 3 2 1 6 5 4 7 

    # Test 42 - reverse in groups recursive
    linked_list = CircularLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(4)
    linked_list.push(5)
    linked_list.push(6)
    #linked_list.reverse_k_recursive(linked_list.head, 3)
    #print(linked_list)
    # Expected output: 3 2 1 6 5 4 7

    # Test 43 - remove duplicates in sorted list
    linked_list = CircularLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(4)
    linked_list.push(4)
    linked_list.push(5)
    linked_list.push(6)
    linked_list.push(6)
    linked_list.push(6)
    linked_list.push(7) 
    linked_list.sortedRemoveDuplicates()
    print(linked_list)
    # Expected output: 1 2 3 4 5 6 7

    # Test 44 - seperate even and odd
    linked_list.seperateEvenOdd()
    print(linked_list)
    # Expected outcome: 1 3 5 7 2 4 6
