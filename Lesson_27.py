import os
import shutil
def create_directory():
    print("Creating directory")
    os.makedirs("Demo", exist_ok=True)
    print()
def write_to_file():
    print("Writing to file: Demo/test.txt")
    with open("Demo/test.txt", "w", encoding="utf-8") as file:
        file.write("This is the content of the file\n")
        print()
def read_from_file():
    print("Reading from file: Demo/test.txt")
    with open("Demo/test.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
def cleanup_directory():
    print("Cleaning up: Removing directory Demo")
    shutil.rmtree("Demo")
if __name__ == "__main__":
    create_directory()
    write_to_file()
    read_from_file()
    cleanup_directory()