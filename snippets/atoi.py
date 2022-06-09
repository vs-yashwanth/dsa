

def atoi(string):           # O(n), O(1)

    sign = -1 if string[0] == '-' else 1
    if sign == -1:
        string = string[1:]

    res = 0
    for i in string:
        if not i.isdigit():
            return 0
        res = res*10 + int(i)
    
    return res*sign

s = "-134"
print(atoi(s))