def main():
    a=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22.15,-4,7]
    low,high,su=maxsub(a,0,len(a)-1)
    print(a[low:high+1],su)
    
def maxcross(a,low,mid,high):
    maxleft=-10000
    sm=0
    for i in range(mid,low-1,-1): 
        sm+=a[i]
        if sm>maxleft:
            maxleft=sm
            low=i
    maxright=-10000
    sm=0
    for i in range(mid+1,high+1):
        sm+=a[i]
        if sm>maxright:
            maxright=sm
            high=i
    return low,high,maxleft+maxright

def maxsub(a,low,high):
    if low==high:
        return low,high,a[low]
    else:
        mid=(low+high)//2
        leftlow,lefthigh,leftsum=maxsub(a,low,mid)
        rightlow,righthigh,rightsum=maxsub(a,mid+1,high)
        crosslow,crosshigh,crosssum=maxcross(a,low,mid,high)
        if leftsum>=rightsum and leftsum>=crosssum:
            return leftlow,lefthigh,leftsum
        elif rightsum>=leftsum and rightsum>=crosssum:
            return rightlow,righthigh,rightsum
        else:
            return crosslow,crosshigh,crosssum
    
main()