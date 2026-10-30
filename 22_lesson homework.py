numbers = input("Enter numbers separated by commas: ")]

for end in range(len(numbers) - 1, 0, -1):
    for index in range(end):
        if numbers[index] > numbers[index + 1]:
            numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]

print("Numbers in ascending order:", numbers)




inputted_list = input("Enter numbers separated by spaces: ").split(" ")
min_value = inputted_list[0]
for x in inputted_list:
    if x < min_value:
        min_value = x
print(min_value) #f"Minimum value is {min_value}")

len_list = len(inputted_list)
index = len_list - 1
for item in inputted_list:
    if inputted_list[index] < 1:
        print(f"Sorted list is the following inputted_list[index]")
    if inputted_list[index] > inputted_list[index - 1]:
        Print(f"{inputed_list[index-1]}, {inputted_list[index]}")
        min_value = item
print(f"Minimum value is {min_value}")