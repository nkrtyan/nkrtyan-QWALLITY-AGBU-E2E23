# During program creation create your own list, tuple, dict, set.
#1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)

array1 = list(map(int, input("Enter list of numbers: ").split()))

new_array1 = []
for i in array1:
    if i not in new_array1: 
        new_array1.append(i)
        
print(f"New list after removing duplicates: {new_array1}")

#2 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.  

array2 = list(map(int, input("Enter list of numbers: ").split()))
## version1
new_array2 = []
for j in range(len(array2)):
    if j != 0 and j != 4 and j != 5:
        new_array2.append(array2[j])

print(f"New list after removing 0th, 4th and 5th elements: {new_array2}")

## version2
index_array = [0, 4, 5]
for index in sorted(index_array, reverse = True):
    del array2[index]
print(f"New list after removing 0th, 4th and 5th elements: {array2}")

#3 Write a Python program to get the difference between the two lists.

print(f"The difference between the two lists:  {list(set(array1) ^ set(array2))}\n")

#4 Write a Python program to convert a tuple to a dictionary.

print(f"Fill the values for the Dictionary. ")
users_tup = ('Name', 'Surname', 'Age')
users_dictionary = {}
for key in users_tup:
    users_values = input(f"{key} - ")
    users_dictionary[key] = users_values
print(users_dictionary)

#5 Write a Python program to add an item in a tuple.

base_tupl = (0, 1, 1)
print(f"Continue the Fibonacci sequence. {base_tupl}")
continue_tupl =  tuple(map(int, input(f"Enter your answer -  ").split()))
full_sequence = base_tupl + continue_tupl
is_correct = True

for item in range(len(full_sequence) - 2):
    if full_sequence[item] + full_sequence[item + 1] != full_sequence[item + 2]:
        is_correct = False
        break
if is_correct:
    print(f"The full Fibonacci sequence after appending numbers in tuple is: {full_sequence}")
else:
    print("Try again :(")

#6 Write a Python program to add a key with value to a dictionary.

users = {
    "Id": 1,
    'Name': input("Enter Name: "),
    'Surname': input("Enter Surname: ")
}

print("Enter additional data")
dictionary_key = input(f"Enter the key of dictionary: ")
dictionary_value = input(f"Enter the value of dictionary: ")
users.update({dictionary_key: dictionary_value})
print(users)

#7 Write a Python program to get the maximum and minimum value in a dictionary().

subjects = {
    'Math': int(input("Enter your grade from Math: ")),
    'Physics': int(input("Enter your grade from Physics: ")),
    'English': int(input("Enter your grade from English: ")),
    'Geography': int(input("Enter your grade from Geography: ")),
}
max_grades = subjects['Math']
min_grades = subjects['Math']
for key in subjects:
    grade = subjects[key]
    if grade > max_grades:
        max_grades = grade
    if grade < max_grades:
        min_grades = grade

print(f"The maximum grade from the subject is - {max_grades}")
print(f"The minimum grade from the subject is - {min_grades}")

#8 Write a Python program to create a union of sets.

student1_set = {'Math', 20, 'English', 19, 'Physics', 16}
student2_set = {'Chemistry', 17, 'Biology', 19, 'Math', 20}

set_of_students = student1_set.union(student2_set)
print(f"The result of the aggregation of students' grades {set_of_students}")

#9 Student  Information
# Write a Python program to create a dictionary with the following
# information about a student:
# ●	name 
# ●	age 
# ●	address 
# ●	education 
# ●	phone_numbers (store two phone numbers in a list) 
# Then:

students_info = {
    'name': input("Enter your Name: "),
    'age': input("Enter your Age: "),
    'Address': input("Enter your Address: "),
    'Education': input("Enter your Education: "),
    'Phone_numbers': input("Enter your Phone_numbers: ").split()
}
#9.1 Print the entire dictionary.

print("9.1 Result of your datas.")
for key, value in students_info.items():
    print(f" '{key}': {value},")

# 9.2.	Print only the student's name. 

print(f"9.2 The name of student - {students_info["name"]}")

# 9.3.	Print only the list of phone numbers. 

print(f"9.3 The last number is - {students_info['Phone_numbers'][-1]}")

# 9.4.	Add a new key called "email" with your email address.

students_info["Email"] = input("Enter your Email address")

# 9.5.	Print the updated dictionary.

print(f"9.5 The dictionary after adding new key and value.")
for key, value in students_info.items():
    print(f" '{key}': {value},")
