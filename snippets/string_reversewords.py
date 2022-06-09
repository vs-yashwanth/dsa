def reverse(S):     # O(n), O(n)

    out = []
    word = ''
    space = ''
    for i in S:
        if i.isspace():
            if word:
                out.append(word)
                word = ''
            space += i
        else:
            if space:
                out.append(space)
                space = ''
            word += i
    if word:
        out.append(word)
    if space:
        out.append(space)
    
    return ''.join(reversed(out))


def reverse2(S):    # O(n), O(n)
    out = ''
    for w in S.split():
        out += ' ' + w[::-1]
    return out[::-1]
    


S = 'geeks for geeks is god tier'
print(reverse(S))
print(reverse2(S))