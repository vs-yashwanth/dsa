def nonrepeating(string):
    non = []
    repeat = [0]*26

    for i in string:
        index = ord(i) - ord('a')
        if not repeat[index] and i not in non:
            non.append(i)
        elif not repeat[index] and i in non:
            non.remove(i)
            repeat[index] = 1
        else:
            pass
        
        if non:
            print('non repeating',non[0])

nonrepeating('geeksforgeeksandgeeksandquizfor')
    

            