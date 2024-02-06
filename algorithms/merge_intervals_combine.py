
def main(ints1, ints2):

    out = []

    i = j = 0

    while i < len(ints1) and j < len(ints2):

        a_in_b = ints1[i][0] >= ints2[j][0] and \
            ints1[i][0] <= ints2[j][1]

        b_in_a = ints2[j][0] >= ints1[i][0] and \
            ints2[j][0] <= ints1[i][1]

        if a_in_b or b_in_a:
            out.append((min(ints1[i][0], ints2[j][0]),
                       min(ints1[i][1], ints2[j][1])))

        if ints1[i][1] < ints2[j][1]:
            i += 1
        else:
            j += 1

    return out


# def main(ints1, ints2):

#     out = []

#     i = j = 0

#     while i < len(ints1) and j < len(ints2):

#         if ints1[i][1] >= ints2[j][0] and ints1[i][0] <= ints2[j][1]:
#             out.append((min(ints1[i][0], ints2[j][0]),
#                        min(ints1[i][1], ints2[j][1])))

#         if ints1[i][1] < ints2[j][1]:
#             i += 1
#         else:
#             j += 1

#     return out


print(main([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))
print(main([[1, 3], [5, 7], [9, 12]], [[5, 10]]))
