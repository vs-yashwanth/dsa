l=[]
maxi = 0
for i in range(0,101,):
    for j in range(0,100-i+1):
        for k in range(0,100-i-j+1):
            cur = 0.5*i+3*j+4*k
            if cur>maxi:
                out = (i/100,j/100,k/100)
                maxi = cur

print(maxi/100,out)
#print(l)