class Box:
    def __init__(self,l,b,h):
        self.l = l
        self.b = b
        self.h = h
    
    def __lt__(self,other):
        return self.l*self.b < other.l*other.b


def stack_boxes(boxes):
    rotated = []
    for box in boxes:
        new_box = Box(0,0,0)
        new_box.h = box.h
        new_box.l = max(box.l, box.b)
        new_box.b = min(box.l,box.b)
        rotated.append(new_box)

        new_box = Box(0,0,0)
        new_box.h = box.l
        new_box.l = max(box.b, box.h)
        new_box.b = min(box.b, box.h)
        rotated.append(new_box)

        new_box = Box(0,0,0)
        new_box.h = box.b
        new_box.l = max(box.l,box.h)
        new_box.b = min(box.l,box.h)
        rotated.append(new_box)

    n = len(rotated)
    rotated.sort(reverse=True)

    height = [box.h for box in rotated]

    for i in range(1,n):
        box = rotated[i]
        for j in range(i):
            sub_box = rotated[j]
            if box.l < sub_box.l and box.b < sub_box.b:
                if height[i] < height[j] + box.h:
                    height[i] = height[j] + box.h
    
    return max(height)


if __name__ == "__main__":
    arr = [Box(4, 6, 7), Box(1, 2, 3), Box(4, 5, 6), Box(10, 12, 32)]
    print(stack_boxes(arr))
           


