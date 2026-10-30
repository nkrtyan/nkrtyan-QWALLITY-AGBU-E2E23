# # initial_list = [1, 55, -2, 1, "aa", "duplicate", 0, "duplicate"]
# # unique_list = []
# # for i in initial_list:
# #     if initial_list[i] == initial_list[i - 1]:
# #         unique_list = unique_list.append(initial_list[i])
# # print(initial_list)
# # print(unique_list)


# # 1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)

# # initial_list = [1, 55, -2, 1, "aa", "duplicate", 0, "duplicate"]
# # unique_list = []
# # for i in (initial_list):
# #     if i not in unique_list:
# #         unique_list.append(i)
# # print(initial_list)
# # print(unique_list)



# # Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.

# # initial_list = [1, 55, -2, 1, "aa", "duplicate", 0, "duplicate"]
# # for index in range(len(initial_list)):
# #     if index == 0 or index == 4 or index == 5:
# #         initial_list.remove(initial_list[index])
# # print(initial_list)


# # initial_list = [1, 55, -2, 1, "aa", "duplicate", 0, "duplicate"]
# # initial_list.remove(initial_list[5]) 
# # initial_list.remove(initial_list[4]) 
# # initial_list.remove(initial_list[0]) 
# # print(initial_list)


# #3 Write a Python program to get the difference between the two lists.
# # List1 = [1, 55, -2, 1, "aa", "duplicate", 0, "duplicate"]
# # List2 = [1, "aa", "duplicate", 0,]
# # dif_list = []
# # for item in List1:
# #     if item not in List2:
# #         dif_list.append(item)
# # print(dif_list)


# List1 = [1, 55, -2, 1, "aa", "duplicate", 0, "duplicate"]
# List2 = [1, "aa", "duplicate", 0,]
# set1 = set(List1)
# set2 = set(List2)
# dif = set1.difference(set2) 
# print(dif)
# print(type(dif))

# # 4 Write a Python program to convert a tuple to a dictionary.
# # my_tuple = ("a", "b", 2)
# # my_dict = {}
# # for index in range(len(my_tuple)):
# #     my_dict[f"Key{index}"] = my_tuple[index]
# # print(my_dict)  


# # 5 Write a Python program to add an item in a tuple.
# # my_tuple = ("a", "b", 2)
# # my_tuple = my_tuple + ("dd",)
# # print(my_tuple)


# # 6 Write a Python program to add a key with value to a dictionary.
# # my_dict = {"Address1": "Street1", "Address2": "Street1"}
# # my_dict["Address3"] = "Street3"
# # print(my_dict)

list = [10, 23, 45, 67, 88, 92, 34, 56, 78, 90]
for i in range(2,6):
    print (f"an indec {i} thr number is {list[i]}")
    