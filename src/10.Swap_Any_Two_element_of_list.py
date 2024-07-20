#Swap_Any_Two_element_of_list
#Approach1 simple swap
# my_list=[23,33,44,55]
# print("List->1 Before Swapping :",my_list)
# pos1,pos2=1,3
# my_list[pos1],my_list[pos2]=my_list[pos2],my_list[pos1]
# print("List->1 after Swapping :",my_list)

#Approach2 pop
# my_list=[23,33,44,55]
# print("List->2 Before Swapping :",my_list)
# pos1,pos2=1,3
# first=my_list.pop(pos1) #33
# Second=my_list.pop(pos2-1) #55
# my_list.insert(pos1,Second)
# my_list.insert(pos2,first)
# print("List->2 After Swapping :",my_list)

#Approach3 Tuple
my_list=[23,33,44,55]
print("List->3 Before Swapping :",my_list)
pos1,pos2=1,3
get=(my_list[pos1],my_list[pos2])
my_list[pos2],my_list[pos1]=get
print("List->3 After Swapping :",my_list)

