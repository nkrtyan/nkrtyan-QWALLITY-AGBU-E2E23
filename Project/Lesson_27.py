import os
import shutil

def create_directory():
    if not os.path.exists("Demo"): # TODO, do not hard code the dir name
        os.makedirs("Demo")
        print("Done") # TODO, need to log instead of just print in all functions

def write_file(): # TODO, file name should be given as an argument
     with open("Demo/test.txt", "w") as file:
         file.write ("This is the content of the file.") # TODO, content also should eb given as an argument
         print ("Done")

def read_file():
    with open("Demo/test.txt", "r") as file: # File name is hard coded
        print(file.read())

if __name__ == "__main__": # TODO, this block shoud be last section, after should not be any function
    create_directory()
    write_file()
    read_file()

    def cleanup():
     answer = input("Delete it? ։ (yes/no) ") # TODO some symbols are not recognised
     if answer == "yes":
        os.remove("Demo/test.txt") # TODO, no need to remove file if you use shutil
        shutil.rmtree("Demo")


if __name__ == "__main__": # TODO, two main block is not allowed in the same file
    cleanup()


