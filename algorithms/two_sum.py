def main():
    a = [1,2,4,7,8]
    k = 5
    print(find1(a,k))
    print(find2(a,k))
    print(find3(a,k))

""" find two nums in a such that sum is k"""
def find1(a,k):  # O(n^2)
    for i in a:
        for j in a:
            if i+j == k and  i!=j:
                return i,j
    return None

def find2(a,k):  # O(nlogn)
    a.sort()
    n = len(a)
    low = 0
    high = n-1
    while low < high:
        now = a[low] + a[high]
        if now < k:
            low += 1
        elif now > k:
            high -= 1
        else:
            return (a[low], a[high])

def find3(a,k):
    s = set()
    for i in a:
        if k-i in s:
            return i,k-i
        else:
            s.add(i)
    return None


main()

    