import heapq as pq

# For ‘K’ employees, we are given a list of intervals representing the working hours of each employee.
# Our goal is to find out if there is a free interval that is common to all employees.
# You can assume that each list of employee working hours is sorted on the start time.


def optimal(employees):  # O(n log k) k-> no of employees

    free_times = []
    working_hours = []
    pq.heapify(working_hours)

    for i in range(len(employees)):
        pq.heappush(working_hours,
                    (employees[i][0][0], employees[i][0][1], i, 1))

    prev = pq.heappop(working_hours)
    if prev[3] < len(employees[prev[2]]):
        pq.heappush(working_hours, (employees[prev[2]][prev[3]]
                    [0], employees[prev[2]][prev[3]][1], i, prev[3]+1))

    while working_hours:
        cur = pq.heappop(working_hours)
        if prev[1] < cur[0]:
            free_times.append((prev[1], cur[0]))
        if cur[3] < len(employees[cur[2]]):
            pq.heappush(
                working_hours, (employees[cur[2]][cur[3]][0], employees[cur[2]][cur[3]][1], i, cur[3]+1))
        prev = cur

    return free_times


def brute_force(employees):  # O(nlogn)

    working_hours = []
    for employee in employees:
        working_hours.extend(employee)

    working_hours.sort(key=lambda x: x[0])

    out = []
    for i in range(1, len(working_hours)):
        if working_hours[i][0] > working_hours[i-1][1]:
            out.append((working_hours[i-1][1], working_hours[i][0]))

    return out


main = optimal
print(main([[[1, 3], [5, 6]], [[2, 3], [6, 8]]]))
print(main([[[1, 3], [9, 12]], [[2, 4]], [[6, 8]]]))
print(main([[[1, 3]], [[2, 4]], [[3, 5], [7, 9]]]))

# [(3, 5)]
# [(4, 6), (8, 9)]
# [(5, 7)]
