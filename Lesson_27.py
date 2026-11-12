import os
import shutil
# TODO, keep lines between functions
# TODO, add logging configuration

def create_directory():
    print("Creating directory")  # TODO, replace print with logging in all functions
    os.makedirs("Demo", exist_ok=True) # TODO, dir name should be given as an argument
    print()  # TODO, remove empty print() in all functions

def write_to_file():  # TODO, take file_path and content as arguments
    print("Writing to file: Demo/test.txt") # TODO,  no need to hardcode
    with open("Demo/test.txt", "w", encoding="utf-8") as file:
        file.write("This is the content of the file\n")
        print()

def read_from_file():
    print("Reading from file: Demo/test.txt")
    with open("Demo/test.txt", "r", encoding="utf-8") as file:  # TODO, handle FileNotFoundError with try/except
        content = file.read()
        print(content)  # TODO, return content instead of print

def cleanup_directory():
    print("Cleaning up: Removing directory Demo")
    shutil.rmtree("Demo")  # TODO, check that directory exists before removing
    # TODO, remove this line and add 2 empty lines before __main__ block

if __name__ == "__main__":
    # TODO, define DIR_NAME and FILE_NAME variables once and pass them to the functions
    create_directory()
    write_to_file()
    read_from_file()  # TODO, save returned content to a variable and log it
    cleanup_directory()  # TODO, call cleanup in "finally" block so it runs even on error
