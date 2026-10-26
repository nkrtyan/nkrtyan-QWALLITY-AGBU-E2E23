
# № 1. 
numbers = [1, 2, 2, 3, 4, 5, 5, 6, 7, -6]
newNumbers = []

for x in numbers:
    if x not in newNumbers:
        newNumbers.append(x)
print(newNumbers)

# № 2. 
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'orange', 'mango', 'pear']

del fruits[4:6]
del fruits[0]
print(fruits)

# for i in [5 ,4, 0]:
#     del fruits[i]

print(fruits)

# № 3. 

list1 = ['apple', 'banana', 'kiwi', 'orange']
list2 = ['banana', 'orange', 'pear']
different = []

for x in list1:
    if x not in list2:
        different.append(x)

for x in list2:
    if x not in list1:
        different.append(x)

print(different)

# second version 
different = set(list1)^set(list2)
print(different)

# № 4. 

myTuple = (('name', 'Anna'), ('name2', 'Tom'))
myDict = {}

for x, y in myTuple:
    # myDict.update({x: y}) or we can
    myDict[x]=y

print(myDict)

print(dict(myTuple))

# № 5. 

myTuple = (('name', 'Anna'), ('name2', 'Tom'))
myTuple2=myTuple + (('name3', 'Anna3') ,)

print(myTuple2)

# № 6. 

myFriends = {
    'name' : 'Lena',
    'name1' :'Lena1',
    'name2' :'Lena2',    
    }

myFriends.update({
    'name3' : 'Lena3',
})
print(myFriends)

# № 7. 
myCount = {
    'TBank' : 2000,
    'ABank' : 10000,
    'BBank' : 40000, 
}

maxi = myCount['TBank']
mini = myCount['TBank']

# print(max(myCount.values()))
# print(min(myCount.values()))

for y in myCount.values():
    if y > maxi:
        maxi = y  
    if y < mini:
        mini = y

print(maxi)
print(mini)


# № 8. 

myInfo = {1, 2 , 3}
myInfo2 = {4, 5 , 6}

allInfo = myInfo | myInfo2
print(allInfo)

# № 9.

student = {
    "name": "Anna",
    "age": 25,
    "address": "Yerevan",
    "education": "University",
    "phone_numbers": ["+374 91 123456", "+374 99 654321"]
}

print(student)
print(student["name"])
print(student["phone_numbers"])

student.update({"mail": "mail@gmail.com"})
print(student)


#1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)

#2 Write a Python program which print a specified list after removing the 0th, 4th and     5th elements.  

#3 Write a Python program to get the difference between the two lists.

#4 Write a Python program to convert a tuple to a dictionary.

#5 Write a Python program to add an item in a tuple.

#6 Write a Python program to add a key with value to a dictionary.

#7 Write a Python program to get the maximum and minimum value in a dictionary().

#8 Write a Python program to create a union of sets.

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






























    






    


