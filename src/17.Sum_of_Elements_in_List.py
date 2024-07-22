#Method1 Using For Loop with range
my_list=[1,2,3,7]
total=0
for i in range(0,len(my_list)):
    total=total+my_list[i]
print("Total Sum of list is",total)

#Method2 Using Only Loop
my_list=[1,2,3,7]
total=0
for i in my_list:
    total=total+i
print("Total Sum of list is", total)

#Method3 Using Sum Method
my_list=[1,2,3,7]
total=sum(my_list)
print("Total Sum of list is", total)