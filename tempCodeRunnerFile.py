mylist = input("input the number")
max1 = mylist[0]
for item in mylist[1:]:
    if  item > max1:
        item = max1
        print(max1)