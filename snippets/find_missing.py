
def missing(A):
    R = range(1,len(A)+2)
    n = len(A)+1
    r = 0
    for i in R:
        r ^= i
    for i in A:
        r ^= i
    print(r)

    s1 = sum(R)
    s2 = sum(A)
    print(s1-s2)

    s1 = n*(n+1)//2
    print(s1-s2)



A = [1, 2, 4, 5, 6]
print(missing(A))