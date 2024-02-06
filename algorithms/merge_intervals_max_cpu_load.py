import heapq as pq

# We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.
# O(nlogn), O(n)


def main(jobs):

    jobs.sort(key=lambda x: x[0])
    cpu = []
    pq.heapify(cpu)
    max_load = 0
    cur_load = 0

    for job in jobs:
        start, end, load = job
        while cpu and cpu[0][0] <= start:
            _, _, out_load = pq.heappop(cpu)
            cur_load -= out_load
        pq.heappush(cpu, (end, start, load))
        cur_load += load
        max_load = max(max_load, cur_load)

    return max_load


print(main([[1, 4, 3], [2, 5, 4], [7, 9, 6]]))
print(main([[6, 7, 10], [2, 4, 11], [8, 12, 15]]))
print(main([[1, 4, 2], [2, 4, 1], [3, 6, 5]]))


# 7
# 15
# 8
