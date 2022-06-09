def gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    if a == b:
        return a
    elif a>b:
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)

def gcd2(a,b):  # O(log(max(a,b)))
    if b==0:
        return a
    return gcd(b, a%b)

def lcm(a,b):
    return a*b // gcd2(a,b)
    
def main():
    a = 15
    b = 20
    print(gcd(a,b))
    print(gcd(a,b))
    print(lcm(a,b))
main()