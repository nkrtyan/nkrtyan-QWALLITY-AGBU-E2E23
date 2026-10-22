#1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)
# mylist = [2, 4, 2, 10, 5, 4, 8, 3, 5]
# newlist = []

# for i in mylist:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)


#2 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.  
# mylist = [2, 5, 14, 8, 3, 10, 1, 7]
# del mylist[5], mylist[4], mylist[0]
# print(mylist)


#3 Write a Python program to get the difference between the two lists.
# mylist1 = [2, 7, 4, 1, 6]
# mylist2 = [1, 5, 2, 3, 4]
# newlist = []

# for i in mylist1:
#     if i not in mylist2:
#         newlist.append(i)
# print(newlist)


#4 Write a Python program to convert a tuple to a dictionary.
# mytuple = (("name", "Nare"), ("age", "15"), ("city", "Yerevan"))
# mydict = dict(mytuple)
# print(mydict) 


#5 Write a Python program to add an item in a tuple.
# solution one
# mytuple  = (1, 4, 10, 7, 9)
# newtuple = (5, 8)
# mytuple += newtuple
# print(mytuple)

# solution two
# mytuple  = (1, 4, 10, 7, 9)
# newtuple = (5, 8)
# mytuple = mytuple[:1] + (5,) + mytuple[1:3] + (8,) + mytuple[3:]
# print(mytuple)


#6 Write a Python program to add a key with value to a dictionary.
# mydict = {"name": "Nare", "age": "15", "city": "Yerevan"}
# mydict["address"] = "Tumanyan 22"
# print(mydict)


#7 Write a Python program to get the maximum and minimum value in a dictionary().
# mydict = {"a": 3, "b": 15, "c": 5, "d": 2}
# print(min(mydict.values()))
# print(max(mydict.values()))


#8 Write a Python program to create a union of sets.
# myset = {"abc", "aaa", "bbb", "xxx"}
# yourset = {"aaa", "fff", "mmm", "abc", "yyy"}
# print(myset.union(yourset))


#9
# mydict = {"name": "Nare", "age": "19", "address": "Teryan 13", "education": "NPUA", "phone_numbers": ["+37498989898","+37493939393"]}
# print(mydict)

# print(mydict["name"])

# print(mydict["phone_numbers"])

# mydict["email"] = "email@gmail.com"

# print(mydict)


