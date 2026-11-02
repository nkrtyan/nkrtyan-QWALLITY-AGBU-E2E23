#Opening, appending and reading the txt file 

# TODO, make a function and give file name as an argumnet, use with open
f=open("new_file.txt", "a+")
f.write ("Hello\nIt's my first file handling!")
f.seek(0)
new=f.read()
print(new) # TODO, variable name is not good

# Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.alphabet_files():
# TODO, the same here ake a function and call it. logic is correct
alphabet_files="ABCDEFGHIGKLMNOPQRSTUVWXYZ"

for i in alphabet_files:
    f=open(f"{i}.txt", "w")
    f.write (f"This is {i} file")
    f.close
        
