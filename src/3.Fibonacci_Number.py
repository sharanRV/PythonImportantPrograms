#A series of a numbers in which each number (Fibonacci Number) is the sum of two preceeding numbers.
n1=int(input("Enter the Number1 : "))
n2=int(input("Enter the number2 : "))

print(n1)
print(n2)

for i in range(2,10):
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum

