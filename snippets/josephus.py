def josephus(n,k):       # O(n)
    if n==1:
        return 1
    else:
        return ( josephus(n-1,k)+k-1 )%n+1
    
print(josephus(16,2))

# after killing 1st we call j(n-1,k) but it assumes 
# position starts at k%n+1(k+1) so we need to 
# compensate