mylist = input("input the number").split()
min1 = int(mylist[0])
for item in mylist[1:]:
    item = int(item)
    if  item < min1:
        min1 = item
print(min1)