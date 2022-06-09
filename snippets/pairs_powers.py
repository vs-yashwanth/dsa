
def count_pairs_naive(x,y,n1,n2):
    count = 0
    for i in x:
        for j in y:
            if i**j > j**i:
                count += 1
    return count











X = [2, 1, 6]
Y = [1, 5]
print("Total pairs = ",count_pairs_naive(X, Y, len(X), len(Y)))