#1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)
ls1 = list(input('Enter elements for List: ').split())

ls1.sort()

for i in range(len(ls1) - 1, 0, -1) :
    if  ls1[i] == ls1[i-1]:
        del ls1[i]

print(f'#1 removed duplicates List is {ls1}\n')            

#2 Write a Python program which print a specified list after removing the 0th, 4th and  5th elements.  

del ls1[5],ls1[4],ls1[0]

print(f'#2 after removing the 0th, 4th and  5th elements {ls1}\n')

#3 Write a Python program to get the difference between the two lists.

ls2 = list(input('Enter elements for List: ').split())

print (f'#3 difference {list(set(ls2) - set(ls1))}\n')

#4 Write a Python program to convert a tuple to a dictionary.

keys = input ('Keys: ').split()
values = input ('Values: ').split()
pairs = []

for i in range(len(keys)):
    pair = (keys[i],values[i])
    pairs.append(pair)

tp1 = tuple(pairs)
dc1 = dict(tp1)    

print(f'#4 tuple to dict: {dc1}\n')

#5 Write a Python program to add an item in a tuple.

tp2 = tuple(input('Enter elements for tuple: ').split())
new_element = input('Enter new element: ')

new_ls = list(tp2)
new_ls.append(new_element)

new_tp2 = tuple(new_ls)
print(f'#5 Updated tuple = {new_tp2}\n')

#6 Write a Python program to add a key with value to a dictionary.

new_key = input ('Key: ')
new_value = input ('Value: ')

dc1[new_key] = [new_value] #from 4 exercise  

print(f'#6 Updated Dict{dc1}\n')

#7 Write a Python program to get the maximum and minimum value in a dictionary().

dc2 = {}

for i in range(len(keys)):
    dc2[keys[i]] = values[i]

dc2_values = list(dc2.values())

max_val = dc2_values[0]
min_val = dc2_values[0]

for val in dc2_values:
    if val > max_val:
        max_val = val
    if val < min_val:
        min_val = val   

print(f'#7 dict max = {max_val},dict min = {min_val}\n')   

#8 Write a Python program to create a union of sets.

set1 = set(input('Enter elements for set1: '))
set2 = set(input('Enter elements for set2: '))

sets_union = set1.union(set2)

print(f'#8 Sets union = {sets_union}\n')

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

name = input("Enter student's name: ")
age = input("Enter student's age: ")
address = input("Enter student's address: ")
education = input("Enter student's education: ")

phone1 = input("Enter first phone number: ")
phone2 = input("Enter second phone number: ")
phone_numbers = [phone1, phone2]

student_information = {'name': name,
                      'age': age,
                      'address': address,
                      'education': education,
                      'phone_numbers':phone_numbers}

print(f'9 student information is {student_information}\n')

print(f'Student name: {student_information['name']},Phone number: {student_information['phone_numbers']}\n')

email_address = input('Enter email address: ')
student_information['email'] = email_address

print(f'Updated Student information {student_information}\n')

