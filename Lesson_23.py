#1 Write a Python program to remove duplicates from a list

my_list = [7,6,32,24,7,6]
unique_list = []

for i in my_list:
    if i not in unique_list:
        unique_list.append(i)

print (unique_list)

#2 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.  

my_list = [1,8,16,3,78,6,14]
new_list = []

for item in range (0,len(my_list)):
    if item !=0 and item !=4 and item !=5:
        new_list.append(my_list[item])

print (new_list)

#3 Write a Python program to get the difference between the two lists.

my_list1 = ["Zara", "Kayseryan","Address"]
my_list2 = ["Zara", "Kayseryan","City", 36, "email"]
new_list = []

for item in my_list1:
    if item not in my_list2:
        new_list.append(item)

for item in my_list2:
     if item not in my_list1:
        new_list.append(item)
       

print (new_list)   

#4 Write a Python program to convert a tuple to a dictionary.

my_tuple = (("name", "Zara"), ("age", 36), ("city", "New York"))
my_dict = {}

for key,value in my_tuple:
    my_dict[key] = value
    

print(my_dict)

#5 Write a Python program to add an item in a tuple.

my_tuple1 = (0,1,2,3)
my_tuple2 = (4,5,6)
new_tuple = my_tuple1 + my_tuple2

print(new_tuple)

#6 Write a Python program to add a key with value to a dictionary.

my_dict = {"colour": "white", "fruit": "apple"}
my_dict["dog"] = "cocker spaniel"

print(my_dict)

#7 Write a Python program to get the maximum and minimum value in a dictionary().

my_dict = {"a": 5, "b": 2, "c": 9}
max_v = 0
min_v = 0

for value in my_dict.values():
    if value > max_v:
        max_v = value
        if value < min_v:
           min_v = value

print (max_v, min_v)


#8 Write a Python program to create a union of sets.

my_set1 ={1,2,"table",3,4}
my_set2 ={1,2,"chair",3,4}        

union_set = set()

for item in my_set1:    union_set.add(item)
for item in my_set2:
    union_set.add(item)

print(union_set)

#9 Student  Information
# Write a Python program to create a dictionary with the following information about a student:
# name 
# age 
# address 
# education 
# phone_numbers (store two phone numbers in a list) 
# Then:
# Print the entire dictionary. 
# Print only the student's name. 
# Print only the list of phone numbers. 
# Add a new key called "email" with your email address. 
# Print the updated dictionary.
# 

student = {
    "name": "Zara",
    "age": 36,
    "address": "Yerevan",
    "education": "Master Degree",
    "phone_numbers": ["00000000"]
}

print(student)


print(student["name"])


print(student["phone_numbers"])


student["email"] = "Zara@example.com"


print(student)

# done


    