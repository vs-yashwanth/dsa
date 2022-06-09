
def karumanchi():
    print('karumanchi')
    print('\n'.join(baseKStrings(3,4)))


def baseKStrings(n,k):
    if n == 0: return n
    if n == 1: return [str(i) for i in range(k)]
    return [ digit+bitstring for digit in baseKStrings(1 ,k) for bitstring in baseKStrings(n-1,k)]

karumanchi()

def yashie():
    print('yashie')
    a = ''
    gen(3,a,4)

def gen(n,a,k):
    if n == 0:
        print(' '.join(a))
        return
    for i in range(k):
        t = a + str(i)
        gen(n-1,t,k)

yashie()


