# check if a string is palindrome
# string has a marker indicating the middle

from stack import StackRaw

def is_palindrome_marker(string, marker):
    i = 0
    j = len(string) - 1
    while string[i] != marker:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    if i==j and string[i] == marker:
        return True
    else: return False


def is_palindrome_marker_gpt(string, marker):
    ind = string.index(marker)
    i = 0
    j = len(string) -1
    while i< ind and j > ind:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True if i==j else False


def is_palindrome_marker_stack(string, marker):
    stack = StackRaw()
    i = 0
    while string[i] != marker:
        stack.push(string[i])
        i += 1
    i+=1
    while i < len(string):
        if string[i] != stack.pop():
            return False
        i += 1
    return True if stack.is_empty() else False


if __name__ == '__main__':

    fn = is_palindrome_marker

    s = 'aabcXcbaa'
    print(fn(s,'X'))
    # expected: True
    s = 'aabcXcbca'
    print(fn(s,'X'))
    # expected: False
    s = 'aabcXca'
    print(fn(s,'X'))
    # expected: False
    s = 'aXcba'
    print(fn(s,'X'))
    # expected: False
    s = 'abcXc'
    print(fn(s,'X'))
    # expected: False