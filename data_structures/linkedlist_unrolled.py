import math

num_elements = 8
max_elements = math.ceil(math.sqrt(num_elements))

class node:
    def __init__(self):

        self.array = [0]*max_elements
        self.next = None
    
    def traverse(self,head):
        while head:
            for i in head.array:
                print(i, end=' ')
            head = head.next


if __name__ == '__main__':
    
    head = node()
    first = node()
    second = node()
    
    head.array[0] = 0
    head.array[1] = 1
    head.array[2] = 2
    
    first.array[0] = 3
    first.array[1] = 4
    first.array[2] = 5

    
    second.array[0] = 6
    second.array[1] = 7
    second.array[2] = 8
    
    head.next = first
    first.next = second
    
    head.traverse(head)
    