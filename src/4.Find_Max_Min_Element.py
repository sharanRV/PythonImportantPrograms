#Find_Max_Element

arr=[30,21,55,77,1,7]
max=arr[0]
n=len(arr)
for i in range(1,n):
     if arr[i]>max:
         max=arr[i]
print("Maximum Element is : ", max)

#Find_Min_Element

arr=[30,21,55,77,1,7]
min=arr[0]
n=len(arr)
for i in range(1,n):
     if arr[i]<min:
         min=arr[i]
print("Minimum Element is : ", min)


