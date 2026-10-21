#1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("List without duplicates:", unique_numbers)


#2 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.  
numbers = [1, 2, 3, 5, 8, 13, 21, 34]
del numbers[5]
del numbers[4]
del numbers[0]
print(numbers)

#3 Write a Python program to get the difference between the two lists.
list1 = input("Enter first list of numbers: ").split()
list2 = input("Enter second list of numbers: ").split()
difference = []
for item in list1:
    if item not in list2:
        difference.append(item)
print("Difference:", difference)


#4 Write a Python program to convert a tuple to a dictionary.
student_tuple = ("name", "Varduhi", "age", 24, "city", "Yerevan")
student_dict = {}
for i in range(0, len(student_tuple), 2):
    student_dict[student_tuple[i]] = student_tuple[i + 1]
print(student_dict)


#5 Write a Python program to add an item in a tuple.
original_tuple = (1, 2, 3)
new_item = 4
new_tuple = original_tuple + (new_item,)
print(new_tuple)


#6 Write a Python program to add a key with value to a dictionary.
student_dict = {
    "name": "Varduhi", 
    "age": 24, 
    "city": "Nor Hachn"}
student_dict["grade"] = "A"
print(student_dict)


#7 Write a Python program to get the maximum and minimum value in a dictionary()
scores = {
    "Anna": 85,
    "Aram": 92,
    "David": 76,
    "Mariam": 98
}
maximum = max(scores.values())
minimum = min(scores.values())
print(f"Maximum value: {maximum}")
print(f"Minimum value: {minimum}")


#8 Write a Python program to create a union of sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1.union(set2)
print(union_set)


#9 Write a Python program to create a dictionary with the following information about a student:

student = {
    "name": "Varduhi",
    "age": 24,
    "address": "Nor Hachn, Armenia",
    "education": "Master's degree in Informatics and Applied Mathematics",
    "phone_numbers": ["+374 77 765760", "+374 77 765761"]
}

# Print the entire dictionary
print(f"Student information: {student}")

# Print only the student's name
print(f"Student name: {student['name']}")

# Print only the phone numbers
print("Phone numbers:", student["phone_numbers"])

# Add an email address
student["email"] = "varduhi@example.com"

# Print the updated dictionary
print(f"Updated student information: {student}")

