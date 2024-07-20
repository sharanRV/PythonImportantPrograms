# Natural Numbers>1
# Number Which has only two factors
# Number should be divided by 1 and itself
num = int(input("Enter the Number : "))
count = 0
if num > 1:
    for i in range(1, num + 1):
        if (num % i) == 0:
            count = count + 1

    if count == 2:
        print("Prime Number")
    else:
        print("Not an Prime Number")
