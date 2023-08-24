def reduce(string,last):
    if len(string)<=1:
        return string
    
    if string[0] == string[1]:
        last = string[0]
        while string[0] == string[1]:
            string = string[1:]
        string = string[1:]


    rem = reduce(string[1:],last)

    if len(rem) != 0 and rem[0] == string[0]:
        last = string[0]
        rem = rem[1:]
        return rem
    
    if len(rem) == 0 and string[0] ==  last:
        return rem
    
    return string[0] + rem


string1 = "geeksforgeeg"
print (reduce(string1,''))