#Factorial using recursion
def main():
    num=int(input('Enter no: '))
    fact=factorial(num)
    print("The factorial is: "+str(fact))    
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
main() 

          
          