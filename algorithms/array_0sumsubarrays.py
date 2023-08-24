def zerosums(A):
    n = len(A)
    D = {}
    run = 0
    out = []
    for i in range(n):
        run += A[i]

        if run == 0:
            out.append(A[:i+1])
        
        if run in D:
            for j in D[run]:
                out.append(A[j:i+1])
            D[run].append(i)
        else:
            D[run] = [i+1]
    return out

if __name__ == '__main__':
    arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
    n = len(arr)
    out = zerosums(arr)
    print(out)

 
