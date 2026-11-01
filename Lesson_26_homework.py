#Opening, appending and reading the txt file 

f=open("new_file.txt", "a+")
f.write ("Hello\nIt's my first file handling!")
f.seek(0)
new=f.read()
print(new)

# Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.alphabet_files():
alphabet_files="ABCDEFGHIGKLMNOPQRSTUVWXYZ"
for i in alphabet_files:
    f=open(f"{i}.txt", "w")
    f.write (f"This is {i} file")
    f.close
        
