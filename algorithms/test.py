def nums(n):
    for i in range(n, 0, -1):
        print(i)


def fact(n):

    total = 1
    for i in range(1, n+1):
        total *= i
    # nums(n)
    return total


n = 625
f = fact(n)

print(len(str(f)) - len(str(f).strip('0')))
print(n//5)
