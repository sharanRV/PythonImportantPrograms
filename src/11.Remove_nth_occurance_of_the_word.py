my_list=['Geeks','for','Geeks']
word='Geeks'
n=2
count=0
for i in range(0,len(my_list)):
    if ((my_list[i]==word)):
            count=count+1
            if count==n:
                del my_list[i]
print("Updated List ",my_list)
