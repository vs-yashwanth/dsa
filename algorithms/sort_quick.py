import random
def main():
    a=random.sample(range(10),6)
    print(a)
    quicksort(a,0,len(a)-1)
    print(a)
def quicksort(a,p,r):
    if p<r:
        q=randpartition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)
def partition(a,p,r):
    x=a[r]
    i=p-1
    for j in range(p,r):
        if a[j]<=x:
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[r]=a[r],a[i+1]
    return i+1
def randpartition(a,p,r):
    q=random.randint(p,r)
    a[q],a[r]=a[r],a[q]
    return partition(a, p, r)
main()

            