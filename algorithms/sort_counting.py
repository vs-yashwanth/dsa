# sorting in linear time
# counting sort
import random
def main():
    k=10
    a=random.sample(range(k),6)    
    print(a)
    b=countsort(a,k)

    print(b)
    print(b==sorted(a))
def countsort(a,k):
    c=[0]*k
    b=[0]*len(a)
    for j in a:
        c[j]+=1
    print(c)
    # each element in c has the count of elements in a
    # if there 3 4's in a, c[4]=3
    for j in range(1,k):
        c[j]+=c[j-1]
    print(c)
    # each element in c represents the number of elements <= its 
    # index value in a
    # if c[4]=10, then there are 10 elements in a that are less than
    # or equal to 4.
    for j in range(len(a)-1,-1,-1):
        b[c[a[j]]-1]=a[j]
        c[a[j]]-=1
    return b
main()
    