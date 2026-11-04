# #0 We have two variables: str1 and str2. Create a new string by swapping the first two characters of each string and print the result. 
# str1 = "xyz"
# str2 = "abc"
# n_str1 = str1[:2] + str2[2:]
# n_str2 = str2[:2] + str1[2:]
# print(f"We have two variables: {str1} and {str2}. The result we have {n_str1} {n_str2}")


# #1 Write a Python program that asks the user for their name and then prints a greeting.
# name = input("Enter your name: ")
# print(f"Hello {name}. Welcome to the program!")

# #2 Ask the user for their name and age, then print their name and the age they will be next year.
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {name}. Next year, you will be {age + 1} years old.")

# #3 Ask the user to enter two numbers, then print their:
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print(f" The sum of numbers is {num1 + num2}\n The difference of numbers is {num1 - num2}\n The product of numbers is {num1 * num2}\n The quotient of numbers is {num1 / num2}")

# #4 Write a program that asks the user to enter the length and width of a rectangle and calculates its area and perimeter.
# length = int(input("Enter the length: "))
# width = int(input("Enter the width: "))
# area = length * width
# perimeter = 2 * (length + width)
# print(f"The area of the rectangle is {area} and the perimeter is {perimeter}.")

# #5 Ask the user to enter a number and determine whether it is positive, negative, or zero.
# number = float(input("Enter a number: "))
# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")
    
# #6 Ask the user to enter an integer and determine whether it is even or odd.
# number = int(input("Enter an integer: "))
# if number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")
    
# #7 Ask the user to enter three numbers and print the largest one.
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# if num1 >= num2 and num1 >= num3:
#     largest = num1
# elif num2 >= num1 and num2 >= num3:
#     largest = num2
# else:
#     largest = num3
# print(f"The largest number is {largest}.")

# #8 Ask the user to enter an exam score from 0 to 100 and display the corresponding grade.
# score = float(input("Enter your exam score (0-100): "))
# if score >= 90 and score <= 100:
#     grade = 'A'
# elif score >= 80 and score <= 89:
#     grade = 'B'
# elif score >= 70 and score <= 79:
#     grade = 'C'
# elif score >= 60 and score <= 69:
#     grade = 'D'
# elif score >= 0 and score <= 59:
#     grade = 'F'
# else:
#     grade = 'Invalid score'
# print(f"Your grade is {grade}.")

# #9 Ask the user to enter a year and determine whether it is a leap year.
# year = int(input("Enter a year: "))
# if year % 400 == 0:
#     print(f"{year} is a leap year.")
# elif year % 100 == 0 and year % 400 != 0:
#     print(f"{year} is not a leap year.")
# elif year % 4 == 0:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
    
# #10 Ask the user to enter a positive integer n. Print every number from 1 to n.
# number = int(input("Enter a positive integer: "))
# for i in range(1, number + 1):
#     print(i)
    
# #11 Ask the user for a positive integer n and calculate the sum of all integers from 1 to n.
# number = int(input("Enter a positive integer: "))
# total = 0
# for i in range(1, number + 1):
#     total += i
# print(f"The sum is {total}.")

# #12 Ask the user to enter a number and print its multiplication table from 1 to 10.
# number = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")
    
# #13 Ask the user to enter a non-negative integer and calculate its factorial.
# number = int(input("Enter a non-negative integer: "))
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
# print(f"The factorial of {number} is {factorial}.")

# #14 Ask the user to enter a positive integer and count how many digits it contains.
# number = int(input("Enter a positive integer: "))
# digit_count = 0
# while number > 0:
#     number //= 10
#     digit_count += 1
# print(f"The number of digits is {digit_count}.")

# #15 Ask the user to enter several integers separated by spaces, then find the largest number.
# numbers = input("Enter numbers: ").split()
# max_value = int(numbers[0])
# for item in numbers:
#     if int(item) > max_value:
#         max_value = int(item)
# print(f"The largest number is {max_value}.")


# #16 Ask the user to enter several numbers separated by spaces and calculate their average.
# numbers = input("Enter numbers: ").split()
# total = int(numbers[0])
# for item in numbers[1:]:
#     total += int(item)
# average = total / len(numbers)
# print(f"The average is {average}.")

# #17 Ask the user to enter a word and print it in reverse order.
# word = input("Enter a word: ")
# print(f"The word in reverse order is {word[::-1]}.")

# #18 Write a program that asks the user to enter a word or sentence and counts how many vowels it contains.
# word = input("Enter a word or sentence: ")
# vowel_count = 0
# for char in word:
#     if char.lower() in "aeiou":
#         vowel_count += 1
# print(f"The number of vowels is {vowel_count}.")

# #19 Write a program that asks the user to enter several integers separated by spaces, then counts how many are even and how many are odd.
# numbers = input("Enter numbers: ").split()
# even_count = 0
# odd_count = 0
# for item in numbers:
#     if int(item) % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(f"The number of even numbers is {even_count} and the number of odd numbers is {odd_count}.")

# #20 Write a program that asks the user to enter integers separated by spaces and finds the smallest number.
# numbers = input("Enter numbers: ").split()
# min_value = int(numbers[0])
# for item in numbers:
#     if int(item) < min_value:
#         min_value = int(item)
# print(f"The smallest number is {min_value}.")

# #21 Write a program that accepts integers separated by spaces and creates a new list containing only unique numbers, preserving their original order.
# numbers = input("Enter numbers: ").split()
# unique_numbers = []
# for item in numbers:
#     if int(item) not in unique_numbers:
#         unique_numbers.append(int(item))
# print(f"The unique numbers are: {unique_numbers}")

# #22 Write a program that asks the user to enter a list of integers and then enter a target number. Count how many times the target number appears in the list.
# numbers = input("Enter numbers: ").split()
# target = int(input("Enter the target number: "))
# count = 0
# for item in numbers:
#     if int(item) == target:
#         count += 1
# print(f"The target number {target} appears {count} times in the list.")

#23 Write a program that asks the user to enter two lists of integers and finds the numbers that appear in both lists, without repeating any result.
# list1 = input("Enter the first list of numbers: ").split()
# list2 = input("Enter the second list of numbers: ").split()
# common_numbers = []
# for item1 in list1:
#     for item2 in list2:
#         if int(item1) == int(item2) and int(item1) not in common_numbers:
#             common_numbers.append(int(item1)) 
# print(f"The common numbers are: {common_numbers}")


my_list = [1, 2, 3, 5, 8, 9]
# new_mylist = my_list.extend([10, 11, 12]) # add new elements in the end of the list
# new_mylist = my_list.append(10) # add new element in the end of the list
# new_mylist = my_list.insert(2, 10) # add new element in the specific index of the list
# new_mylist = my_list.remove(5) # remove the specific element from the list
# new_mylist = my_list.pop(2) # remove the specific index element from the list
# new_mylist = my_list.clear() # remove all elements from the list
# new_mylist = my_list.sort() # sort the list in ascending order
# new_mylist = my_list.reverse() # reverse the list
# new_mylist = my_list.find(5) # find the specific element in the list
# my_list[2] = 10 # change the specific index element in the list
# new_mylist = my_list[2:5] # get the specific index elements from the list
# new_mylist = my_list.slice(2, 5) # get the specific index elements from the list
# new_mylist = my_list.split(", ")
# print(f"The new list is: {new_mylist}")

# text = "1, 2, 3, 5, 8, 9"
# my_list = text.split("3, ")
# print(f"The new list is: {my_list}")



#####################################################################################################################################################
# import sys
# import csv
# import pandas

# f = open("myfile.txt", "r")
# data = f.read()
# print(data)


# print(sys.getdefaultencoding())


#Create new txt file add lines and read the file
# lines_to_write = ["line 1", "line 2", "line 3"]
# f = open("myfile.txt", "wt")
# f.writelines(line + "\n" for line in lines_to_write)
# f.seek(0)


# f = open("myfile.txt", "rt")
# data = f.read()
# print(data)
# f.close()


# f = open("myfile.txt", "w+")
# f.write("line4")
# f.seek(0)
# data = f.read()
# print(data)
#seek(0) return line4 but seek(1) return ine4

# with open("myfile.txt", "a") as addline:
#     print(addline.write("\nHello new version"))
    
#Write data to csv

# data = [
#     ["Name", "Age", "City"],
#     ["Varduhi", 24, "Nor Hachn"],
#     ["Rob", 25, "Los Angeles"],
#     ["Ann", 30, "New York"]
# ]

# with open("file.csv", "w", newline='') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerows(data)
# print("Data has been written to the CSV file. ")

# #read and print data to the CSV file
# with open("file.csv", "r", newline='') as csvfile_r:
#     csvreader = csv.reader(csvfile_r)

#     for row in csvreader:
#         print(row)


# write data to excel
# data = {
#     "Name": ["Ani", "Varduhi", "Armine"],
#     "Age": [20, 24, 30],
#     "City": ["Yerevan", "Nor Hachn", "New York"]
# }

# df = pandas.DataFrame(data)
# df.to_excel("newfile.xlsx", index = False)
# print("Data has been written to the excel file.")

# read_df = pandas.read_excel("newfile.xlsx")
# print(read_df)