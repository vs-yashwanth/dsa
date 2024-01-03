def reverse(Q):
    aux = []
    n = len(Q)
    for _ in range(n):
        for _ in range(len(Q)-1):
            Q.append(Q.pop(0))
        aux.append(Q.pop(0))
    return aux
        
    

q = [1,2,3,4,5,6]
print(reverse(q))