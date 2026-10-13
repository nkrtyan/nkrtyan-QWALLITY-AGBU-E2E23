number_list = input("Enter a list of numbers separated by spaces: ").split()
# print(type(number_list))
# print(f"List of numbers: {number_list}")


# Find the maximum number in the list
max_number = number_list[0]

for number in number_list[1:]:
    if number > max_number:
        max_number = number
print(f"Max number is: {max_number}")


# Find the minimum number in the list
min_number = number_list[0]

for numb2 in number_list[1:]:
    if numb2 < min_number:

        min_number = numb2
print(f"Min number is: {min_number}")


# Sort the list of numbers in ascending order

for i in number_list:
    index = 0

    for j in number_list[:-1]:
        if number_list[index] > number_list[index + 1]:
            temp1 = number_list[index]
            number_list[index] = number_list[index + 1]
            number_list[index + 1] = temp1

        index += 1

print(f"Sorted list: {number_list}")
