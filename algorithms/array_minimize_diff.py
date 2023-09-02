# minimize the max diff between elements by
# either + or - k

def minimize(A,k):
    A.sort()
    out = A[-1] - A[0]
    maxi = mini = 0
    for i in range(1,len(A)):
        mini = min(A[0]+k, A[i]-k)
        maxi = max(A[i-1]+k,A[-1]-k)
        out = min(out,maxi-mini)
    return out


arr=[1, 10, 14, 14, 14, 15]
k=6
print(minimize(arr,k))
