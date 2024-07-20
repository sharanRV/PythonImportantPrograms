#Search_An_Element_In_List
#Approach1 using for loop
my_List=[3,4,5,9,7]
ele=int(input("Enter the element: "))
# flag=0
# for i in range(0,len(my_List)):
#     if (my_List[i]==ele):
#         print("Element Found")
#         flag=1
#         break
# if flag==0:
#     print("Element Not Found")

#Approach 2 using In Method
if ele in my_List:
    print("Element Found")
else:
    print("Element Not Found")