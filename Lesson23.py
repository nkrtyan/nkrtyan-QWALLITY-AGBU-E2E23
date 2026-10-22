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
