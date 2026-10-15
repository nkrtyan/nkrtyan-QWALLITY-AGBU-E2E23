my_list = [int(x) for x in input("input the number").split()]
min_1 = my_list[0]
for item in my_list[1:]:
    if item < min_1:
        min_1 = item
print(min_1) 