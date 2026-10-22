
mylist = [1,3,5,6,4]
newlist = []

num = mylist[0]
for i in mylist[1:]:
    if i < num:
        num = i
newlist.append(num)
mylist.remove(num)

# num = mylist[0]
# for i in mylist[1:]:
#     if i < num:
#         num = i
# newlist.append(num)
# mylist.remove(num)

# num = mylist[0]
# for i in mylist[1:]:
#     if i < num:
#         num = i
# newlist.append(num)
# mylist.remove(num)

# num = mylist[0]
# for i in mylist[1:]:
#     if i < num:
#         num = i
# newlist.append(num)
# mylist.remove(num)

# num = mylist[0]
# for i in mylist[1:]:
#     if i < num:
#         num = i
# newlist.append(num)
# mylist.remove(num)

newlist.append(mylist[0])

print(newlist)

