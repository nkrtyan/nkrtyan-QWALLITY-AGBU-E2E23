import os
import shutil

def create_directory():
    if not os.path.exists("Demo"):
        os.makedirs("Demo")
        print("Done")

def write_file():
     with open("Demo/test.txt", "w") as file:
         file.write ("This is the content of the file.")
         print ("Done")

def read_file():
    with open("Demo/test.txt", "r") as file:

        print(file.read())

if __name__ == "__main__":
    create_directory()
    write_file()
    read_file()

    def cleanup():
     answer = input("Delete it? ։ (yes/no) ")
     if answer == "yes":
        os.remove("Demo/test.txt")
        shutil.rmtree("Demo")


if __name__ == "__main__":
    cleanup()


