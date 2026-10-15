inputted_list = input("Enter numbers separated by spaces: ").split(" ")
min_value = inputted_list[0]
for x in inputted_list:
    if x < min_value:
        min_value = x
print(f"Minimum value is {min_value}")
