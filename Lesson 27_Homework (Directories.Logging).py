import os
import shutil

def directory_creation(directory_name):
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)


def file_writing(name_of_file):
    with open(name_of_file, "w+", encoding = "utf-8") as file:
        file.write("This is the content of the file.")


def file_reading(file_name):
    with open(file_name, "r", encoding = "utf-8") as file:
            file_content = file.read()
            print(file_content)


def cleanup(name_root):
    ask_to_user = input("Would you like remove created folder with folders,put Yes/No: ")
    if ask_to_user.lower() == "yes":
        if os.path.exists(name_root):
            shutil.rmtree((name_root))
            print(f"Directory {name_root} and all its contents have been removed.")

import logging

logging.basicConfig(

    format="%(asctime)s--------%(levelname)s--------%(message)s",
    level = logging.INFO,
    filename =os.path.join("Demo", "logging_information")
)        


if __name__ == "__main__":

    directory_creation("Demo")
    logging.info("Directory creation function executed")   

    file_path = os.path.join("Demo", "test.txt")

    file_writing(file_path)
    logging.info("Nested file created and content added successfully")  

    file_reading(file_path)
    logging.info("Nested file reading completed")

    cleanup("Demo")
    logging.info("Directory deleted successfully")   

# How to add also warning and error after logging.info's ?
# I have tried with if but not worked well

