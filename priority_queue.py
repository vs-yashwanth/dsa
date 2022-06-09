def return_max(H):
    return H[0]
def extract_max(H):
    maxi = H.pop(0)
    n=len(H)
    heapify(H,n,0)
    return maxi
def heapify(H,n,i):
    l=i*2+1
    r=l+1
    if l<n and H[l]>H[i]:
        largest=l
    else:largest=i
    if r<n and H[r]>H[largest]:
        largest=r
    if i!=largest:
        H[i],H[largest]=H[largest],H[i]
        heapify(H,n,largest)
def priority_queue():
    H=[5,3,6,2,1,4]
    for i in range(len(H)):
        heapify(H,len(H),i)
    for _ in range(len(H)):
        print(extract_max(H))
    
priority_queue() 