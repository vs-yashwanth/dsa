def main():
    s = [1,2,3,4,5,6]
    rev(s)
    print(s)

def rev(s):
    if s:
        temp = s.pop()
        rev(s)
        add_bottom(s,temp)
def add_bottom(s,temp):
    if not s:
        s.append(temp)
    else:
        temp2 = s.pop()
        add_bottom(s,temp)
        s.append(temp2)
    
main()