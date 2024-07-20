#Clear_a_List
#Approach1
# my_list=[3,6,7,9,11]
# print("Before Clearing the List ",my_list)
# my_list.clear()
# print("After Clearing the List ",my_list)

#Approach2
# my_list=[3,6,7,9,11]
# print("Before Clearing the List ",my_list)
# my_list=[]
# print("After Clearing the List ",my_list)

#Approach3
# my_list=[3,6,7,9,11]
# print("Before Clearing the List ",my_list)
# my_list *=0
# print("After Clearing the List ",my_list)

#Approach4
my_list=[3,6,7,9,11]
print("Before Clearing the List ",my_list)
del my_list[:]
print("After Clearing the List ",my_list)