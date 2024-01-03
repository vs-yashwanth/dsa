from stack import StackRaw


def remove_duplicates(string):  # O(n), O(n)
    stack = StackRaw()
    for i in string:
        if stack.is_empty() or stack.peek() != i:
            stack.push(i)
        else:
            stack.pop()
    stack.reverse()
    out = ''
    while not stack.is_empty():
        out += stack.pop()
    return out


if __name__ == '__main__':
    print(remove_duplicates(list('careermonk')))
    print(remove_duplicates(list('mississippi')))
