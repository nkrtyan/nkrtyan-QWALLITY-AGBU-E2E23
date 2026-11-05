import os
import shutil 
import logging # FIX, move "import logging" here, all imports should be at the top
                # FIX, move connfiguration to the top

logging.basicConfig(

    format="%(asctime)s--------%(levelname)s--------%(message)s",
    level = logging.INFO,
    filename = "execution_log.log"  # FIX , don't save log file in "Demo": folder doesn't exist yet and it will be deleted by cleanup, also add .log extension
)  

def directory_creation(directory_name):  
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
        logging.info(f"Directory {directory_name} creation function executed") 
    else:
         logging.warning(f"Directory {directory_name} already exists")    


def file_writing(name_of_file):
    with open(name_of_file, "w+", encoding="utf-8") as file:  # FIX, no spaces around "=" for function arguments in all places: encoding="utf-8"
        file.write("This is the content of the file.")
        logging.info(f"Nested file {name_of_file} created and content added.") 
        # FIX, add logging in all functions


def file_reading(file_name):
    with open(file_name, "r", encoding = "utf-8") as file:
            file_content = file.read()  
            print(file_content)
            logging.info(f"Nested file {file_name} read") 

def cleanup(name_root):
    ask_to_user = input("Would you like remove created folder with folders,put Yes/No: ")
    if ask_to_user.lower() == "yes":
        if os.path.exists(name_root):
            shutil.rmtree(name_root)  # FIX, remove extra brackets
            print(f"Directory {name_root} and all its contents have been removed.")
            logging.info("Directory deleted successfully") 
            return True
        else:
            logging.warning("Deletion was not completed")         
            return False
    else:
        logging.info("User cancelled directory deletion")
        return False        


if __name__ == "__main__":

    logging.info('Program started')
    my_direcory_name = "Demo"

    directory_creation(my_direcory_name)  #FIX, save "Demo" in a variable and use it in all places

    file_path = os.path.join(my_direcory_name, "test.txt")

    file_writing(file_path) 

    if os.path.exists(file_path):
        logging.info("File created successfully")
        file_reading(file_path)
    else:
        logging.error("File was not created")
    

    cleanup(my_direcory_name)  # FIX, return True/False from cleanup, then use if/else: logging.info if deleted, logging.warning if not

    logging.info("Program finished")     


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
