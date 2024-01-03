from stack import StackRaw


def max_area_brute(hist):  # O(n^2)
    max_area = 0
    for i in range(len(hist)):
        left = i - 1
        while left >= 0 and hist[i] <= hist[left]:
            left -= 1
        right = i+1
        while right < len(hist) and hist[i] <= hist[right]:
            right += 1
        max_area = max(max_area, hist[i]*(right-left-1))
    return max_area


# for each find left and right smaller values to get the width
def max_area_stack(hist):  # O(n), O(n)

    max_area = 0
    stack = StackRaw()
    i = 0
    n = len(hist)
    while i<n:
        if stack.is_empty() or hist[i] >= hist[stack.peek()]:
            stack.push(i)
            i+=1 
        else:
            top = stack.pop()
            cur_area = hist[top] * (i if stack.is_empty() else i-stack.peek()-1)
            max_area = max(cur_area, max_area)
    while not stack.is_empty():
        top = stack.pop()
        cur_area = hist[top] * (i if stack.is_empty() else n-stack.peek()-1)
        max_area = max(max_area, cur_area)
    return max_area


if __name__ == '__main__':

    max_area = max_area_stack

    histogram_1 = [1, 2, 3, 4, 5]
    print(max_area(histogram_1))
    # Output: 9 (Area of the rectangle formed by bars with heights 3, 4, and 5)

    histogram_2 = [5, 4, 3, 2, 1]

    print(max_area(histogram_2))
    # Output: 9 (Same as the previous case)

    histogram_3 = [2, 1, 5, 6, 2, 3]
    print(max_area(histogram_3))
    # Output: 10 (Largest area is formed by bars with heights 5 and 6)

    histogram_4 = [6, 2, 5, 4, 5, 1, 6]
    print(max_area(histogram_4))
    # Output: 12 (Largest area is formed by bars with heights 5, 4, and 5)

    histogram_5 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print(max_area(histogram_5))
    # Output: 15 (Largest area is formed by bars with heights 1 through 5)

    histogram_6 = [2, 2, 2, 2, 2]
    print(max_area(histogram_6))
    # Output: 10 (Largest area is formed by all bars with height 2)
