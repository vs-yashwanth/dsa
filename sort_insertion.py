import random

def main():
    # print(random.sample.__doc__)
    a = list(random.sample(range(1, 10),6))

    print(a)

    inssort(a)
    print(a==sorted(a))
    

def inssort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
        print(a)
main()