# Method1:using loops
my_list=[1,2,3,4,5,6,7,10,8,9,10,11,10]
n=10
count=0
for ele in my_list:
    if (ele==n):
        count=count+1
print("{} has Occured {}times".format(n,count))

#Method2 using count method
my_list=[1,2,3,4,5,6,7,10,8,9,10,11,10]
n=10
print("{} has occured {}times".format(n,my_list.count(n)))

#Method3:Using Counter Method
from collections import Counter
my_list=[1,2,3,4,5,6,7,10,8,9,10,11,10,11]
n=11
dict=Counter(my_list)
print(dict)
print("{} has Occured {} times".format(n,dict[n]))



