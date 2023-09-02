import random
a=list(random.sample(range(1,7),6))
#a=[4,2,6,3,1,5]
print(a)

"""for i in range(len(a)-1):
    m=10
    j=i
    while j<len(a):
        if a[j]<m:
            m=a[j]
            a[j]=a[i]
            a[i]=m
        j+=1
    print(a)"""
    
for i in range(len(a)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(a)): 
        if a[min_idx] > a[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    a[i], a[min_idx] = a[min_idx], a[i] 
    print(a)
        