def equify(a,b):
    s1 = sum(a)
    s2 = sum(b)
    diff = (s1-s2)//2
    print(s1,s2,diff)
    if diff>=0:
        a = set(a)
        for i in b:
            if i+diff in a:
                return (i,i+diff)
    else:
        b = set(b)
        diff *= -1
        for i in a:
            if i+diff in b:
                return (i,i+diff)
    return -1

A=[4,1,2,1,1,2]
B=[3,6,3,3]
 
# Call to function
print(equify(A,B))


    