# import sys
# print(sys.getdefaultencoding())
# 1
def new_file():
    with open("new_file.txt", "a") as file:
        file.write("Hello\n")
        file.write("it's my first file handling!\n")
    with open("new_file.txt", "r") as file: # TODO, code duplication, instead of opening again the same file, use seek(0)
        read_file = file.read()
        print(read_file)
new_file()

# 2
import string
def create_alphabet_files():
    for alpha in string.ascii_uppercase:
        with open(f"{alpha}.txt", "w") as file:
            file.write(alpha)

create_alphabet_files() # Nel, correct

# TODO, no need to commit the files created by code