# matrix multiplication
# using numpy
import numpy as np
a=np.ones((3,3))
b=np.ones((3,3))
c=a.dot(b)
print('with numpy: ')
print(a,b,c,sep='\n\n')
# with nested loops
d=np.zeros((3,3))
for i in range(3):
    for j in range(3):
        for k in range(3):
            d[i][j]+=a[i][k]*b[k][j]
print('\nwith nested loops:')
print(d)

# with list comprehension
e= [[sum(i*j for i,j in zip(rows,cols)) for cols in zip(*b)] for rows in a ]
print('\nwith list comprehension:')
print(e)