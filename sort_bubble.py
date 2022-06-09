import random
def main():
    # print(random.sample.__doc__)
    a = list(random.sample(range(1, 10), 6))

    print(a)

    bubblesort(a)
    print(a)
    print(a == sorted(a))
def bubblesort(a):
    for i in range(len(a)):
        flag=False
        for j in range(len(a)-1,i,-1):
            if a[j-1]>a[j]:
                a[j],a[j-1]=a[j-1],a[j]
                flag=True
        if not flag:
            break
        print(a)
main()