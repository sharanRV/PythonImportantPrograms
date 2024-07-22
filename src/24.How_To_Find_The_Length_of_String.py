#Method1 using for loop
# str="sharan"
# count=0
# for i in str:
#     count=count+1
# print("Length Of The String : ",count)

#Method2 using while loop
str="sharan"
count=0
while str[count:]:
    count=count+1
print("Length Of The String : ",count)

#Method3 using len() method
str="sharan"
print("Length Of The String :",len(str))
