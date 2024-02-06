
def main(intervals, new_int):

    n = len(intervals)
    start, end = new_int
    out = []

    i = 0
    while i < n and start > intervals[i][1]:
        out.append(intervals[i])
        i += 1

    while i < n and end >= intervals[i][0]:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1

    out.append((start, end))

    while i < n:
        out.append(intervals[i])
        i += 1

    return out


print(main([[1, 3], [5, 7], [8, 12]], [4, 6]))
print(main([[1, 3], [5, 7], [8, 12]], [4, 10]))
print(main([[2, 3], [5, 7]], [1, 4]))
