#Check String Is Palindrome Or Not
string=input("Enter the string : ")
rev=string[::-1]
if string==rev:
    print("Palindrome String")
else:
    print("Not An Palindrome String")