def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)



def main():
    a = 10
    b = 15
    print(gcd(a,b))
