def max_num(s,d):

    out = ''
    for _ in range(d):
        s -= 9
        out += '9'
        if s<0:
            s += 9
            out = out[:-1]
            out += str(s)
            break
    return out

s = 20
m = 3
print(max_num(s,m)) 