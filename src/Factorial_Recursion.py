#Factorial_Recursion
#5*4*3*2*1

def factorial(n):
#Approach1
    # if (n==0 or n==1):
    #     return 1
    # else:
    #     return n * factorial(n-1)
#Approach2
#Ternary Operator
     return 1 if(n==0 or n==1) else  n * factorial(n-1)
num=int(input("Enter the Number : "))
print("The Factorial of ",num,"is",factorial(num))