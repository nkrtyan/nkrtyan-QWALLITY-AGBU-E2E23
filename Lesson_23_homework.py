# # 1 Write a Python program to remove duplicates from a list
# numbers = input("Enter a list of numbers separated by spaces: ").split()

# new_list = []

# for i in numbers:
#     count = 0

#     for j in new_list:
#         if i == j:
#             count = count + 1

#     if count == 0:
#         new_list.append(i)

# print(new_list)

# # 2 Write a Python program which print a specified list after removing the 0th, 4th and     5th elements.
# numbers = input("Enter numbers: ").split()

# if len(numbers) > 5:
#     numbers.pop(5)

# if len(numbers) > 4:
#     numbers.pop(4)

# if len(numbers) > 0:
#     numbers.pop(0)

# print(numbers)

# # 3 Write a Python program to get the difference between the two lists.
# list1 = input("Enter the first list of numbers separated by spaces: ").split()
# list2 = input("Enter the second list of numbers separated by spaces: ").split()

# difference = []

# for i in list1:
#     if i not in list2:
#         difference.append(i)

# for i in list2:
#     if i not in list1:
#         difference.append(i)

# print(difference)


# 4 Write a Python program to convert a tuple to a dictionary.
# my_tuple = (
#     ("name", "Mariam"),
#     (23, "age"),
#     ("country", "Armenia"),
#     ("city", "Yerevan"),
# )

# my_dict = {}

# for item in my_tuple:
#     if isinstance(item[0], int):
#         my_dict[item[1]] = item[0]
#     else:
#         my_dict[item[0]] = item[1]


# print(my_dict)


# or
# my_dict = dict(my_tuple)

# print(my_dict)
# print(type(my_dict))


# 5 Write a Python program to add an item in a tuple.
# my_tuple = tuple(input("Enter a tuple of items separated by spaces: ").split())
# item_to_add = tuple(input("Enter an item to add: ").split())

# my_new_tuple = my_tuple + item_to_add

# print(my_new_tuple)

# # 6 Write a Python program to add a key with value to a dictionary.
# my_dict = {"name": "Mariam", "age": 23, "country": "Armenia"}

# my_dict["city"] = "Yerevan"
# my_dict["name"] = "Mariam A."

# print(my_dict)

# # 7 Write a Python program to get the maximum and minimum value in a dictionary().
# my_dict = {"a": 10, "b": 20, "c": 5, "d": 15}
# print("Maximum value:", max(my_dict.values()))
# print("Minimum value:", min(my_dict.values()))


# # 8 Write a Python program to create a union of sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)

print(f"Union of sets: {union_set}")

# Create a dictionary with student information
student = {
    "name": "Mariam",
    "age": 23,
    "address": "Yerevan",
    "education": " Master's in Software Engineering",
    "phone_numbers": ["1021323721", "58382721"],
}

# Print the entire dictionary
print(student)

# # Print the student's name
print("The student's name is:", student["name"])

# # Print the phone numbers
print("The student's phone numbers are:", student["phone_numbers"])

# # Add email to the dictionary
student["email"] = "mariam@example.com"

# # Print the updated dictionary
print("The updated student dictionary is:", student)
