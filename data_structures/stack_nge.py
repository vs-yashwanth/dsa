from stack import StackRaw


def nge_brute(array):  # O(n^2)
    out = []
    for i in range(len(array)):
        nge = -1
        for j in array[i+1:]:
            if j > array[i]:
                nge = j
                break
        out.append(nge)
    return out


def nge_stack(array):  #
    stack = StackRaw()
    out = []
    for i in array:
        while not stack.is_empty() and stack.peek() < i:
            out.append((stack.pop(), i))
        stack.push(i)

    while not stack.is_empty():
        out.append((stack.pop(), -1))
    return out


if __name__ == '__main__':

    nge = nge_stack

    print(nge([4, 5, 2, 25]))  # expected: [5, 25, 25, -1]
    print(nge([11, 13, 21, 3]))  # expected: [13, 21, -1, -1]
    print(nge([4, 5, 2, 10, 8]))  # expected: [5, 10, 10, -1, -1]
    print(nge([3, 9, 7, 4, 6, 8]))  # expected: [9, -1, 8, 6, 8, -1]
    print(nge([2, 1, 5, 7, 3, 9]))  # expected: [5, 5, 7, 9, 9, -1]
    print(nge([6, 8, 3, 2, 5]))  # expected: [8, -1, 5, 5, -1]
    print(nge([10, 4, 6, 12, 9]))  # expected: [12, 6, 12, -1, -1]
