import heapq as pq


def main(employees):

    working_hours = []
    for employee in employees:
        working_hours.extend(employee)
    
    working_hours.sort(key= lambda x:x[0])

    out = []
    for i in range(1, len(working_hours)):
        if working_hours[i][0] > working_hours[i-1][1]:
            out.append((working_hours[i-1][1], working_hours[i][0]))
    
    return out


print(main([[[1, 3], [5, 6]], [[2, 3], [6, 8]]]))
print(main([[[1,3], [9,12]], [[2,4]], [[6,8]]]))
print(main([[[1, 3]], [[2, 4]], [[3, 5], [7, 9]]]))


