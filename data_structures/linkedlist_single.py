class Node:
    def __init__(self, val):
        self.val =  val
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def pushLeft(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    
    def __str__(self):
        out = ''
        cur = self.head
        while cur:
            out += f'{cur.val} '
            cur = cur.next
        return out
    
    def length(self):
        out = 0
        cur = self.head
        while cur:
            out += 1
            cur = cur.next
        return out
    
    def insert(self, ind, val):
        length = self.length()
        if ind>length : return
        elif ind == length: 
            self.push(val)
            return
        if ind == 0: 
            self.pushLeft(val)
            return
    
        node = Node(val)
        cur = self.head
        for _ in range(ind-1):
            cur = cur.next
        if cur:
            node.next = cur.next
            cur.next = node

    
    def pop(self):
        cur = self.head
        if not cur: return
        while cur.next and cur.next.next:
            cur = cur.next
        out = cur.next
        cur.next = None
        return out.val
        
    def popLeft(self):
        out = self.head
        self.head = self.head.next
        return out.val
    
    
    def remove(self, val):
        cur = self.head
        while cur.next and cur.next.val != val:
            cur = cur.next

        if cur.next:
            cur.next = cur.next.next

    def removeAt(self, ind):
        length = self.length()
        if ind>=length: return
        elif ind == length-1:
            self.pop()
            return
        elif ind == 0:
            self.popLeft()
            return

        cur = self.head
        for _ in range(ind-1):
            cur = cur.next
        
        cur.next = cur.next.next
        
    
    def fromEnd(self, ind):
        cur = self.head
        fast = cur
        for _ in range(ind):
            if fast:
                fast = fast.next
            else: return
        while fast.next:
            fast = fast.next
            cur = cur.next
        return cur.val
    
    def middle(self): 
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.val

    def reversePrint(self, node = None): 
        if not node:
            return
        self.reversePrint(node.next)
        print(node.val, end=' ')
        if node ==  self.head: print()
        return

    def reverse(self) : 
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev
        

    def reverseRecursive(self, head):
        if head and head.next:
            self.reverseRecursive(head.next)
            head.next.next = head
            head.next = None
        else: 
            self.head = head

            

    def sum(self):
        total = 0
        cur = self.head
        while cur :
            if type(cur.val) is int or type(cur.val) is float:
                total += cur.val
            else: return None
            cur = cur.next
        
        return total

    def sumRecursive(self, node):
        if not node: return 0
        return node.val + self.sumRecursive(node.next)

    def isALoop(self):
        slow =  self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
   
   

if __name__ == '__main__':

    # Tests from ChatGPT :)

    linked_list = SingleLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(4)

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
    linked_list_single_element = SingleLinkedList()
    linked_list_single_element.push(99)
    middle_value_single_element = linked_list_single_element.middle()
    # Expected output: middle_value_single_element = 99
    print(f"middle_value_single_element = {middle_value_single_element}")

    # Test 25: Get the middle element from the modified linked list
    middle_value_modified = linked_list.middle()
    # Expected output: middle_value_modified = 2
    print(f"middle_value_modified = {middle_value_modified}")

    # Test 26: Create a new linked list with multiple elements and get its middle
    linked_list_multiple_elements = SingleLinkedList()
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
        invalid_linked_list = SingleLinkedList()
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
    linked_list = SingleLinkedList()
    linked_list.push(6.5)
    linked_list.push(8.2)
    linked_list.push(9)
    linked_list.push(4.7)
    linked_list.push(3)
    linked_list.push(2)

    total_sum_recursive = linked_list.sumRecursive(linked_list.head)
    # Expected output: total_sum_recursive = 33.4 (sum of 5 + 1 + 2 + 3 + 6.5 + 8.2 + 9 + 4.7 + 3 + 2)
    print(f"total_sum_recursive = {total_sum_recursive}")


    # Test 32: Check if the linked list has a loop using 'isALoop'
    print(linked_list.isALoop())
    # Expected output: False (No loop in the linked list)

    # Test 33: Create a loop in the linked list and check again
    linked_list.head.next.next.next.next.next.next = linked_list.head.next
    print(linked_list.isALoop())
    # Expected output: True (Loop exists in the linked list)