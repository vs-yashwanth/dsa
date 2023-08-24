def main():
    a=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22.15,-4,7]
    n=len(a)
    start,end,s=kadane(a)
    print(a[start:end+1],s)
    start,end,s=dnq(a,0,n-1)
    print(a[start:end+1],s)
    
def kadane(a):     # O(n)
    here = a[0]
    best = a[0]
    s=0
    for i in range(1,len(a)):
        here+=a[i]
        if here>best:
            best=here
            start=s
            end=i
        if here<0:
            here=0
            s=i+1
    return start,end,best

def dnq(a,low,high):    
    if low==high:
        return low,low,a[low]
    else:
        mid=(low+high)//2
        leftlow,lefthigh,leftsum = dnq(a,low,mid)
        rightlow,righthigh,rightsum = dnq(a,mid+1,high)
        crosslow,crosshigh,crosssum = dnqcross(a,low,mid,high)
        
        if rightsum<=leftsum>=crosssum:
            return leftlow,lefthigh,leftsum
        elif leftsum<=rightsum>=crosssum:
            return rightlow,righthigh,rightsum
        else:
            return crosslow,crosshigh,crosssum

def dnqcross(a,low,mid,high):
    leftmax=-10000
    s=0
    for i in range(mid,low-1,-1):
        s+=a[i]
        if s>leftmax:
            leftmax=s
            low=i
    rightmax=-10000
    s=0
    for i in range(mid+1,high+1):
        s+=a[i]
        if s>rightmax:
            rightmax=s
            high=i
    return low,high,leftmax+rightmax
    
main()
        
    
    