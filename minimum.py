mylist = input("Enter your number:")
min0 = mylist[0]
for i in mylist[1:]:
    if i < min0:
        min0 = i
print(min0)
