def generate(n,array,i):
    if i == n:
        print(' '.join([str(i) for i in array]))
        return
    
    array[i] = 0
    generate(n,array,i+1)

    array[i] = 1
    generate(n,array,i+1)

if __name__ == '__main__':
    n = 4
    array = [None]*n
    generate(n,array, 0)