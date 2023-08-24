import random
def main():
    a=[]
    for _ in range(10):
        a.append(random.random())
    print(a)
    bucketsort(a)
    print(a)
    print(a==sorted(a))
    
def bucketsort(a):

    b=[]
    for i in range(10):
        b.append([])
    for i in a:
        index=int(i*10)

        b[index].append(i)

    for i in range(10):
        b[i].sort()
    a.clear()
    for i in b:
        for j in i:
            a.append(j)
            
main()