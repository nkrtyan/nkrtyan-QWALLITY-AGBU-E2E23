import os
import shutil  # TODO, move "import logging" here, all imports should be at the top

def directory_creation(directory_name):  
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)


def file_writing(name_of_file):
    with open(name_of_file, "w+", encoding = "utf-8") as file:  # TODO, no spaces around "=" for function arguments in all places: encoding="utf-8"
        file.write("This is the content of the file.")
        # TODO, add logging in all functions


def file_reading(file_name):
    with open(file_name, "r", encoding = "utf-8") as file:
            file_content = file.read()  
            print(file_content)


def cleanup(name_root):
    ask_to_user = input("Would you like remove created folder with folders,put Yes/No: ")
    if ask_to_user.lower() == "yes":
        if os.path.exists(name_root):
            shutil.rmtree((name_root))  # TODO, remove extra brackets
            print(f"Directory {name_root} and all its contents have been removed.")

import logging

# TODO, move connfiguration to the top
logging.basicConfig(

    format="%(asctime)s--------%(levelname)s--------%(message)s",
    level = logging.INFO,
    filename =os.path.join("Demo", "logging_information")  # TODO, don't save log file in "Demo": folder doesn't exist yet and it will be deleted by cleanup, also add .log extension
)        


if __name__ == "__main__":

    directory_creation("Demo")  # TODO, save "Demo" in a variable and use it in all places
    logging.info("Directory creation function executed")   

    file_path = os.path.join("Demo", "test.txt")

    file_writing(file_path)
    logging.info("Nested file created and content added successfully")  

    file_reading(file_path)
    logging.info("Nested file reading completed")

    cleanup("Demo")  # TODO, return True/False from cleanup, then use if/else: logging.info if deleted, logging.warning if not
    logging.info("Directory deleted successfully")   

# How to add also warning and error after logging.info's ?
# I have tried with if but not worked well

# ANSWER:
# "if" is the right idea, but "if" needs a value to check.
# Your function should return that value, then check it in __main__.
#
# Example:
#
# if __name__ == "__main__":
#     is_deleted = cleanup("Demo")
#     if is_deleted:
#         logging.info("Directory deleted successfully")
#     else:
#         logging.warning("Directory was not deleted")
#
# Use the same way for other functions:
# if os.path.exists(file_path):
#     logging.info("File created successfully")
# else:
#     logging.error("File was not created")
#
