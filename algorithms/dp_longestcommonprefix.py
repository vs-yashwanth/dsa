def wordbyword(strings):        #  O(n*m)
    
    pre = strings[0]
    for i in range(1, len(strings)):
        pre = prefix(pre, strings[i])
    return pre



def prefix(s1,s2):
    m = len(s1)
    n = len(s2)
    i = j = 0
    res = ''
    while i<m and j<n:
        if s1[i] == s2[j]:
            res += s1[i]
            i += 1
            j += 1
        else:
            break

    return res

        
if __name__ =="__main__":
 
    arr = ["geeksforgeeks", "geeks",   "geek", "geezer"]
    n = len(arr)

    print(wordbyword(arr))