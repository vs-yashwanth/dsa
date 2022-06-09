def possible(S):
    D = {}
    for i in S:
        if i not in D:
            D[i] = 0
        D[i] += 1
    freqs = list(D.values())
    return max(freqs)-min(freqs)==1

if __name__ == "__main__":
    str1 = "xxxxyyzz"
    print(possible(str1))
