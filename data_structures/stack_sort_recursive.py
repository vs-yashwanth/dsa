def main():
    a = [6,5,4,2,3,1]
    sort_recursive(a)
    print(a)

def sort_recursive(s):
    if s:
        temp = s.pop()
        sort_recursive(s)
        sorted_insert(s,temp)

def sorted_insert(s,temp):
    if not s or temp > s[-1]:
        s.append(temp)
    else:
        temp2 = s.pop()
        sorted_insert(s,temp)
        s.append(temp2)

main()
    