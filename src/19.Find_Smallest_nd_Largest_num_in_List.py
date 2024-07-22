#smallest_and_Largest_num_in_list

#Approach1 sort the list in ascending order and print the list in first and last element
my_list=[9,6,2,3]
my_list.sort()
print(my_list)

print("smallest number in List ",my_list[0])
print("Largest num in List ",my_list[-1])

#Approach2 using min and mx element
my_list=[9,6,2,3]

print("Smallest number in List ",min(my_list))
print("Largest number in List ",max(my_list))


