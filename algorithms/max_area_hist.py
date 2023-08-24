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

hist = [11,11,10,10,10]
print(histy(hist))
