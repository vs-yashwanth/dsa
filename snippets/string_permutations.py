def permute(S,l,r):
    if l==r:
        print(''.join(S))
    else:
        for i in range(l,r+1):
            S[i],S[l] = S[l], S[i]
            permute(S,l+1,r)
            S[i],S[l] = S[l], S[i]


S = 'yash'
permute(list(S),0,len(S)-1)

    
