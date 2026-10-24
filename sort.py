mylist = [5, 2, 8, 1, 3]

for i in range(len(mylist)):
    for j in range(len(mylist) - 1):
        if mylist[j] > mylist[j + 1]:
            temp = mylist[j]
            mylist[j] = mylist[j + 1]
            mylist[j + 1] = temp

print(mylist)

