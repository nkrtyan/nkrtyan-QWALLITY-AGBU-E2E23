list_1=["Ann", "John", "Mia","Ann", "Leo"] #1
without_duplicates=[]
for i in list_1: 
    if i not in without_duplicates:
        without_duplicates.append(i)
print("Names without duplicates:", without_duplicates)

list_2=["apple", "kiwi", "cherry", "orange", "banana", "grape", "peach"] #2
index_to_remove=[5,4,0]
for index in index_to_remove:
    del list_2[index]
print("List after removing elements:", list_2)

list_3=["cat", "dog", "fish", "bird", "tiger"]#3
list_4=["cat", "lion", "dog", "elephant"]
difference= list(set(list_3) - set(list_4))
print ( "Difference between list_3 and list_4:", difference)

tup_1=((1,"dog"),(2, "cat"), (3, "fish")) #4/1
converted_tuple=dict(tup_1)
print("Converted tuple to dictionary:", converted_tuple)

tup_2=("dog", "cat", "fish")#4/2
converted_tuple_2=dict(enumerate(tup_2))
print("Converted tuple to dictionary:", converted_tuple_2)

tup_3=(1,2,3,4,5) #5
tup_4=tup_3+(7,)
print("Added element to tuple:", tup_4)

dict_1={"name":"John", "age":30, "city":"New York"} #6
dict_1["job"]="Engineer"
print("Updated dictionary:", dict_1)

dict_2=[{"name":"John", "age":30, }, {"name":"Alice", "age":23}, {"name":"Mike", "age": 44}] #7
max_age=max(item["age"] for item in dict_2)
min_age=min(item["age"] for item in dict_2)
print("Maximum age:", max_age)
print("Minimum age:", min_age)

set_1={"apple", "banana", "cherry"} #8
set_2={"banana", "kiwi", "orange"}
union_set=set_1.union(set_2) 
print("Union of sets:", union_set)   

dict_3={"name": "Ann", "age": 29, "address": "ABC Street", "education": "Bachelor's Degree" , "phone_number":[1232345, 6789012]} #9
print(dict_3)
print(dict_3["name"])
print (dict_3["phone_number"])
dict_3["email"]="knarikavetyan@gmail.com"
print("Updated dictionary:", dict_3)