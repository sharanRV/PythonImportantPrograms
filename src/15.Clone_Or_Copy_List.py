#Approach1 using slicing technique
my_list=[23,45,78,90]
my_list_copy=my_list[:]
print(my_list_copy)
#Approach2 using extend() method
my_list=[23,45,78,90]
my_list_copy=[]
my_list_copy.extend(my_list)
print(my_list_copy)
#Approach3 using list() method
my_list=[23,45,78,90]
my_list_copy=list(my_list)
print((my_list_copy))
#Approach4 using copy()method
my_list=[23,45,78,90]
my_list_copy=my_list.copy()
print(my_list_copy)
#Approach5 using list comprehension
my_list=[23,45,78,90]
my_list_copy=[i for i in my_list]
print(my_list_copy)