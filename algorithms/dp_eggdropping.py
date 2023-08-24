def naive(eggs,floors):         # O(2**n), O(1)
    if floors<=1:
        return floors
    if eggs == 1:
        return floors
    mini= float('inf')
    for floor in range(1,floors+1):
        res = 1+ max(naive(eggs-1,floor-1),naive(eggs,floors-floor))
        mini = min(mini,res)
    return mini

def bottomup(eggs,floors):          # O(n*k**2), O(n*k)
    table = [[0 for _ in range(eggs+1)] for _ in range(floors+1)]
    for i in range(1,eggs+1):
        table[0][i] = 0
        table[1][i] = 1
    for i in range(1,floors+1):
        table[i][1] = i
    
    for egg in range(2,eggs+1):
        for floor in range(2,floors+1):
            table[floor][egg] = float('inf')
            for f in range(1,floor+1):
                res = 1 + max(table[f-1][egg-1], table[floor-f][egg])
                table[floor][egg] = min(table[floor][egg], res)
    return table[floors][eggs]


if __name__ == "__main__":
 
    n = 2
    k = 10
    print(naive(n, k))
    print(bottomup(n,k))
