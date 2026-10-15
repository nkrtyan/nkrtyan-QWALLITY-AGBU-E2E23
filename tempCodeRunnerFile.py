list=[4,2,7,9,1]
sorted_list=[]
for item in (list):
    min_value = list[0]
    for item in list:
        if item < min_value:
            min_value = item
    sorted_list.append(min_value)
    list.remove(min_value)

print(sorted_list)
