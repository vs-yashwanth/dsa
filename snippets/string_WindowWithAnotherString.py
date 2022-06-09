
def window(s1,s2):

    l1 = [0]*256
    l2 = [0]*256

    for i in s2:
        l2[ord(i)] += 1
    count = start = 0
    start_index = -1
    mini = float('inf')

    for i,e in enumerate(s1):
        l1[ord(e)]+=1
        if l1[ord(e)] <= l2[ord(e)]:
            count += 1
        if count == len(s2):
            while l1[ord(s1[start])] > l2[ord(s1[start])] or l2[ord(s1[start])] == 0:
                if l1[ord(s1[start])] > l2[ord(s1[start])] :
                    l1[ord(s1[start])] -= 1
                start += 1
            new_win = i-start + 1
            if mini>new_win:
                mini = new_win
                start_index = start

    if start_index == -1:
        return -1
    return s1[start_index:start_index+mini]


if __name__ == "__main__":
 
    string = "this is a test string"
    pat = "tist"
 
    print(window(string, pat))






