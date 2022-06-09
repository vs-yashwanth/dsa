def hashing(array):         # O(nlogn), O(n)

    swaps = 0
    D = {j:i for i,j in enumerate(array)}
    sort = sorted(array)
    for i in range(len(array)):
        if array[i] != sort[i]:
            swaps += 1
            now = array[i]
            array[i], array[D[sort[i]]] = array[D[sort[i]]], array[i]
            D[now] = D[sort[i]]
            D[sort[i]] = i
    return swaps

if __name__ == "__main__":
      a = [101, 758, 315, 730, 472, 619, 460, 479]
      n = len(a)
       
      # Output will be 5
      print(hashing(a))

