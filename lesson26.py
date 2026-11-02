#Task1
# TODO, make a function and as an argument take  file name
with open("newfile.txt", "w+") as file:
    file.writelines("Hello" + "\nIt's my first file handling!")
    
with open("newfile.txt", "r") as read_file: # TODO, code duplication, when you open task use seek(0) to go up of the file and read it
    data = read_file.read()
    print(data)

#Task2: Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.
def create_files():
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        with open(f"{letter}.txt", "w") as file:
            file.write(letter)
            
create_files()
# Nel, this part is correct