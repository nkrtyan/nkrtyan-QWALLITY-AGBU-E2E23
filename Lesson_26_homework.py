#Opening, appending and reading the txt file 

# DONE, make a function and give file name as an argumnet, use with open
f=open("new_file.txt", "a+")
f.write ("Hello\nIt's my first file handling!")
f.seek(0)
new=f.read()
print(new) # DONE, variable name is not good

with open("new_file.txt", "a+") as f:
    f.write("\nThis is the second line")
    f.seek(0)
    new_line=f.read()
    print(new_line) 


# Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.alphabet_files():
# DONE, the same here ake a function and call it. logic is correct

def open_alphabet_files():
    alphabet_files="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in alphabet_files:
        with open(f"{letter}.txt", "w") as f:
            f.write(f"This is {letter} file")

open_alphabet_files()