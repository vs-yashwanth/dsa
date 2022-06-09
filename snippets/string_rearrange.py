import heapq

def rearrange(string):
    D = {}
    for i in string:
        if i not in D:
            D[i] = 0
        D[i] -= 1
    q = []
    for i in D:
        heapq.heappush(q,(D[i],i))

    prev = None
    out = ''
    while q:

        char = heapq.heappop(q)
        if prev and prev[0] < 0:
            heapq.heappush(q,prev)

        prev = (char[0]+1,char[1])
        out += char[1]
    return out


print(rearrange('helloworld'))        