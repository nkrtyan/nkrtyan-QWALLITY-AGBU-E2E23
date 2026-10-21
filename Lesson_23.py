new_list = [5,8,8,5,4,2,1]
unique_list = []

for i in new_list:
    duplicate = False
    for j in unique_list:
           if i == j:
               duplicate = True
    if duplicate == False:
           unique_list.append(i)
   
   
print(unique_list)