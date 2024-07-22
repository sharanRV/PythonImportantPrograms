#Method1 Multiply_All_Numbers_In_List
my_list=[1,2,3]
result=1
for i in my_list:
    result=result*i
print("Multiply Numbers in list",result)


#Method2 Multiply_All_Numbers_using Numpy
import numpy
my_list=[1,2,3]
result=numpy.prod(my_list)
print("Multiply Numbers in list",result)