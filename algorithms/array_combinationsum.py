def combination_sum(A, target):
    A = sorted(list(set(A)))
    out = []
    temp = []
    index = 0
    find(A,target,out,temp,index)
    return out

def find(A,target,out,temp,index):
    if target == 0:
        out.append(temp.copy())
        return
    for i in range(index,len(A)):
        if target - A[i] >= 0:
            temp.append(A[i])
            find(A,target-A[i],out,temp,i)
            temp.pop()


arr = [2, 4, 6, 8]
target = 8
ans = combination_sum(arr, target)
print(ans)
