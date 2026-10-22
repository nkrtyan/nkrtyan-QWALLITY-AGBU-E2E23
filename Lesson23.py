# Write a program which will join two tuples and will print reversed joined tuple.
# Option 1
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
tuple3 = tuple1+tuple2
print(tuple3[::-1])

# Option 2
tuple1 = ("Apple", "Banana", "Mango")
tuple2 = ("Cherry", "Tangerine","Grape")
joined_tuple = tuple1 + tuple2
reversed_tuple = joined_tuple[::-1]
print(reversed_tuple)

# Option 3
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
tuple3 = tuple1 + tuple2
reversed_tuple = tuple(reversed(tuple3))
print(reversed_tuple)

# Option 4
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple(reversed(tuple3)))

# Create a list of your favorite fruits. Print the third fruit in the list, add existing fruit to the list, then print list without duplicates.
# Option 1
favorite_fruits = ["Orange", "Peach", "Strawberry", "Mango", "Grapes"]
print("Third fruit:", favorite_fruits[2])
favorite_fruits.append("Peach")
unique_fruits = list(set(favorite_fruits))
print("List without duplicates:", unique_fruits)

# Option 2
favorite_fruits = ["Orange", "Peach", "Strawberry", "Mango", "Grapes"]
print("Third fruit:", favorite_fruits[2])
favorite_fruits.append("Peach")
favorite_fruits = list(dict.fromkeys(favorite_fruits))
print("List without duplicates:", favorite_fruits)

favorite_fruits = ["Orange", "Peach", "Strawberry", "Mango", "Grapes"]
print("Third fruit:", favorite_fruits[3])
favorite_fruits.append(("Tangerine", "Peach"))
favorite_fruits = list(dict.fromkeys(favorite_fruits))
print("List without duplicates:", favorite_fruits)

favorite_fruits = ["Orange", "Peach", "Strawberry", "Mango", "Grapes"]
print("Third fruit:", favorite_fruits[3])
favorite_fruits.append("Tangerine")
favorite_fruits.append("Peach")
favorite_fruits = list(dict.fromkeys(favorite_fruits))
print("List without duplicates:", favorite_fruits)

# Create a Python program that stores and displays a list of classmates with their names and surnames.
classmates_info = [
    {"name": "Arevik", "surname": "Hakobyan"},
    {"name": "Ani", "surname": "Nahapetyan"},
    {"name": "Narek", "surname": "Sargsyan"}
]
print(classmates_info)

# Option without dict
classmates_info = [
    ("Arevik", "Hakobyan"),
    ("Ani", "Nahapetyan"),
    ("Narek", "Sargsyan")
]

print(classmates_info)

#1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set.
num = [11, 21, 31, 11, 22, 23, 21, 33]
unique_num = []
for num in num:
    if num not in unique_num:
        unique_num.append(num)
print(unique_num)

fruits = ["Apple", "Orange", "Pear", "Orange", "Peach", "Grapes", "Apple"]
unique_fruits = []
for fruits in fruits:
    if fruits not in unique_fruits:
        unique_fruits.append(fruits)
print(unique_fruits)

#2 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.  
numbers = [11, 12, 13, 14, 15, 16, 17, 18]
numbers.pop(5)
numbers.pop(4)
numbers.pop(0)
print(numbers)

numbers = [11, 12, 13, 14, 15, 16, 17, 18]
del numbers[5]
del numbers[4]
del numbers[0]
print(numbers)

fruits = ["Apple", "Orange", "Pear", "Peach", "Grapes", "Mango", "Banana"]
fruits.pop(5)
fruits.pop(4)
fruits.pop(0)
print(fruits)

#3 Write a Python program to get the difference between the two lists.
list1 = [11, 12, 13, 14, 15, 16]
list2 = [9, 10, 13, 17, 18, 19]
difference = []
for number in list2:
    if number not in list1:
        difference.append(number)
print(difference)

#4 Write a Python program to convert a tuple to a dictionary.
my_tuple = (("name", "Arevik"), ("surname", "Hakobyan"), ("age", 25))
my_dict = dict(my_tuple)
print(my_dict)