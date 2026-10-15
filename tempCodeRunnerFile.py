my_list = input("Input a list of numbers separated by spaces: ").split()
min_value = my_list[0]
for value in my_list:
    if value < min_value:
        min_value = value
print(min_value) #I know sth is mising, but I got lost. Sorting should have been included here.