#Python Collections-> List, Tuple
#Create python script  which will implement max, min and sort method algorithm.
#Do not use ready max(), min(),  sort() functions

numbers = input("Enter list of numbers: ").split(" ")

max_num = int(numbers[0])
min_num = int(numbers[0])
for i in numbers[1:]:
    #Maximum number from the list
    if int(i) > max_num:
        max_num = int(i)
    
    #Minimum number in the list
    if int(i) < min_num:
        min_num = int(i)

#Sort the numbers from the list by ascending 
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
for i in numbers:
    for j in range(len(numbers) - 1):
        # Bubble Sort
        if numbers[j] > numbers[j + 1]:
            new_list = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = new_list

print(f"Maximum number from the list: {max_num}")
print(f"Minimum number from the list: {min_num}")
print(f"The numbers are arranged in ascending order {numbers}") 
