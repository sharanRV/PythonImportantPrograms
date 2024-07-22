#find_substring_present_In_A_String
#find() Method finds the first Occurance of Specified Value
#find() Method returns -1 if the Value is not found
str=input("Enter the String : ")
sub_str=input("Enter the Sub_String : ")

print(str.find(sub_str))
if str.find(sub_str)==-1:
    print("Str not Found")
else:
    print("{} found".format(sub_str))

