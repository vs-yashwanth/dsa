import random

def binsearch(a,p,r,x):
	if r>=p:
		q=(r+p)//2
		if a[q]==x:
			return q
		elif a[q]>x:
			return binsearch(a,p,q-1,x)
		else:
			return binsearch(a,q+1,r,x)
	else:
		return -1

def main():
	a=sorted(random.sample(range(10),6))
	x=sum(random.sample(a,1))
	print(a,'\nSearched :',x,"\n",binsearch(a,0,len(a)-1,x))
main() 