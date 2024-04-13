import heapq as pq

# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.


def main(intervals):

    intervals.sort(key=lambda x: x[0])
    max_rooms = -float('inf')
    rooms = []
    pq.heapify(rooms)

    for int in intervals:
        int_start, int_end = int
        pq.heappush(rooms, (int_end, int_start))
        while rooms and int_start >= rooms[0][0]:
            pq.heappop(rooms)
        max_rooms = max(max_rooms, len(rooms))

    return max_rooms


print(main([[1, 4], [2, 5], [7, 9]]))
print(main([[6, 7], [2, 4], [8, 12]]))
print(main([[1, 4], [2, 3], [3, 6]]))
print(main([[4, 5], [2, 3], [2, 4], [3, 5]]))
print(main([(0, 10), (10, 20), (20, 30), (30, 40), (40, 50), (50, 60), (60, 70), (70, 80),
      (80, 90), (90, 100), (0, 100), (10, 90), (20, 80), (30, 70), (40, 60), (50, 50)]))

# 2
# 1
# 2
# 2
# 6
