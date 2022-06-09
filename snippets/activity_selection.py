def select(activites):              # O(nlogn)
    activites.sort(key = lambda x: x[1])
    order = []
    order.append(activites[0])
    prev = activites[0]
    for i in range(1,len(activites)):
        if activites[i][0] >= prev[1]:
            order.append(activites[i])
            prev = activites[i]
    return order

Activity = [[5, 9], [1, 2], [3, 4], [0, 6],[5, 7], [8, 9]]
print(select(Activity))