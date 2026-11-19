#Task1
def file_handling(file_name):
    with open(file_name, "w+") as file:
        file.writelines("Hello" + "\nIt's my first file handling!")
    
        file.seek(0)
        data = file.read()
        print(data)

file_handling("my_file.txt")

#Task2: Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.
def create_files():
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        with open(f"{letter}.txt", "w") as file:
            file.write(letter)
            
create_files()
# Nel, this part is correct