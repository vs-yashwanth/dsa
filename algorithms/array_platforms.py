
def plats(arr,dep,n):  # O(nlogn)
    arr.sort()
    dep.sort()
    plats = 1
    maxi = plats
    i = 1
    j = 0
    while i<n and j<n:
        if arr[i] < dep[j]:
            plats += 1
            i += 1
        elif arr[i] > dep[j]:
            plats -= 1
            j += 1
        maxi = max(maxi,plats)
            
    return maxi


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)
 
print(plats(arr, dep, n))
