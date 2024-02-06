import heapq as pq

# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.


def main(intervals):

    intervals.sort(key=lambda x: x[0])
    max_rooms = -float('inf')
    rooms = []
    pq.heapify(rooms)

    for int in intervals:
        int_start, int_end = int
        while rooms and int_start >= rooms[0][0]:
            pq.heappop(rooms)
        pq.heappush(rooms, (int_end, int_start))
        max_rooms = max(max_rooms, len(rooms))

    return max_rooms


print(main([[1, 4], [2, 5], [7, 9]]))
print(main([[6, 7], [2, 4], [8, 12]]))
print(main([[1, 4], [2, 3], [3, 6]]))
print(main([[4, 5], [2, 3], [2, 4], [3, 5]]))
