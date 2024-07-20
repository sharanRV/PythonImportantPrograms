#Swap_first_and_last_element_of_list
my_list=[12,24,36,48,50] #index starts from 0
#Approach1 tempararory variable
print("List Before Swapping :",my_list)
size=len(my_list)
# temp=my_list[0]
# my_list[0]=my_list[size-1]
# my_list[size-1]=temp
# print("List->1 after Swapping :",my_list)

#Approach2
# my_list[0],my_list[size-1]=my_list[size-1],my_list[0]
# print("List-2 after Swapping :",my_list)

# #Approach3 using tuple
# get=(my_list[0],my_list[size-1]) #packing 24 ,50
# my_list[size-1],my_list[0]=get
# print("List->3 after Swapping :",my_list)
#
# #Approach4 *Operands
# my_list=[12,24,36,48,50]
# start,*middle,end=my_list
# my_list=[end,*middle,start]
# print("List->4 after Swapping :",my_list)

#Approach5 pop
my_list=[12,24,36,48,50]
first=my_list.pop(0) #12
last=my_list.pop(-1) #50
my_list.insert(0,last)
my_list.append(first)
print("List->5 after Swapping :",my_list)