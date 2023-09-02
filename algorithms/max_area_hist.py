def histy(hist):
    n = len(hist)
    stack = []
    i = 0
    area = 0
    while i < n:
        if not stack or hist[stack[-1]] <= hist[i]:
            stack.append(i)
            i += 1
        else:
            temp = stack.pop()
            current = hist[temp]*(i-stack[-1]-1) if stack else hist[temp]
            area = max(area, current)

    while stack:
        temp = stack.pop()
        current = hist[temp]*(i-stack[-1]-1) if stack else hist[temp]
        area = max(area, current)
    return area

def max_area_histogram(heights):
    stack = []
    max_area = 0
    i = 0

    while i < len(heights):
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, heights[top] * width)

    while stack:
        top = stack.pop()
        width = i if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, heights[top] * width)

    return max_area

hist = [6, 2, 5, 4, 5, 1, 6]
print(histy(hist))
