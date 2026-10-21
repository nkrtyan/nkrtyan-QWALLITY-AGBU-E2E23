string1="abc"
string2="xyz"
new_string1=string2[:2]+string1[2:]
new_string2=string1[:2]+string2[2:]
print(new_string1, " ", new_string2)

my_list= (0, -1, 5, 10, -2)
max_1= my_list[0]
for item in my_list[1:]:
    if item > max_1:
        max_1=item
print(max_1)

my_list=(input("Enter a list of numbers"))
max_2=my_list[0]
for item in my_list:
    if item > max_2:
        max_2=item
print(max_2)

list1= [4,2,7,9,1] 
min_1= list1[0]
for item in list1[1:]:
    if item < min_1:
        min_1=item  
print(min_1)

list=[4,2,7,9,1]
sorted_list=[]
for i in range(len(list)):
    min_value = list[0]
    for item in list:
        if item < min_value:
            min_value = item
    sorted_list.append(min_value)
    list.remove(min_value)
print(sorted_list)
