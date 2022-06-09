def remove(S):   # O(n), O(n)
    s = set()
    out = ''
    for i in S:
        if i not in s:
            s.add(i)
            out += i
    return out

def remove2(S):   # O(n), O(1)

    S = list(S)
    l = [0 for _ in range(26)]
    for i in S:
        index = ord(i) - ord('a')
        l[index] = 1
    i = j = 0
    while j<len(S):
        index = ord(S[j]) - ord('a')
        if l[index]:
            l[index] = 0
            S[i] = S[j]
            i += 1
        j += 1
    return ''.join(S[:i])



print(remove('geeksforgeeks'))

print(remove2('geeksforgeeks'))
