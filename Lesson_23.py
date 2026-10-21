#1-----------
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
#2-------------
new_list = ["apple","ne_apple","new","Green","Yellow","pinapple","auto"]
new_list.pop(5)
new_list.pop(4)
new_list.pop(0)
print(new_list)

#3-----------
list1 = [3, 4, 5 ,6, 7, 8, 9]
list2 = [7, 8, 9, 10, 11, 12, 13]
new = []
for i in list1:
        if i not in list2:
         new.append(i)
         
print(new)

  #4----------------
my_tuple = (('apple',1), ('new',2), ('girl',3))
new_dict = dict(my_tuple)
print(new_dict)  

#5--------------
my_tup = (3, 4, 5 ,6, 7)
tup = (8,9,10)
new_tup = my_tup + tup
print(new_tup)   
       
#6 ------------
my_dic = {'i':1, 'you':2,}
my_dic['she'] = 3
print(my_dic)
#7---------
my_dic = {'i': 1, 'you': 2, 'she': 3}

print(max(my_dic.values()))
print(min(my_dic.values()))
#8----------
my_set1 = {'i', 'you', 'she', 'it'}
my_set2 = {'i','you','he'}

my_union = my_set1.union(my_set2)
print(my_union)
#9-----------
student = {
    "name": "Anahit",
    "age": 25,
    "address": "Yerevan",
    "education": "Engineering",
    "phone_numbers": ["091123456", "077123456"]
}



print(student)
print(student["name"])
print(student["phone_numbers"])
student["email"] = "anahit@example.com"
print(student)