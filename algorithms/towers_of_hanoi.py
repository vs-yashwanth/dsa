def main():
    #n=int(input('Enter no. of discs: '))
    n=3
    FIRST=1
    TEMP=2
    LAST=3
    
    play(n,FIRST,LAST,TEMP)

def play(n,FIRST,LAST,TEMP):
    if n>0:
        play(n-1,FIRST,TEMP,LAST)
        print('move a disc from',FIRST,'to',LAST)
        play(n-1,TEMP,LAST,FIRST)
main()
