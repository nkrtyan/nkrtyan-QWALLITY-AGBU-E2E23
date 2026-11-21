import os
import shutil
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S', 
    filename='my_log.log',
    filemode='a+', 
    encoding='utf-8' 
)

def create_directory(direct_name):
    if not os.path.exists(direct_name):
        os.mkdir(direct_name)
        logging.info(f"The directory with this names {direct_name} was created succesfully.")
    else:
        logging.warning(f"The directory with this name {direct_name}, already exists.")

def file_writing(f_name, text):
    if not os.path.exists(f_name):
        os.chdir(directory_name)
        with open(f_name, "w") as file:
            file.write(text)
        logging.info(f"The File with this {f_name} name, was created succesfully.")
    else:
        logging.warning(f"The file with this name {f_name}, already exists.")

def file_reading(f_name, text):
    with open(f_name, "r") as file:
        read_text = file.read()
        print(read_text)
        logging.info(f"The File with this {f_name} name, has been read succesfully, and the text is: {text}.")

def cleanup(direct_name):
    question = input("Do you want to delete direction? yes or no: ")
    if question == "yes":
        os.chdir("..")
        if os.path.exists(direct_name):
            shutil.rmtree(direct_name)
            logging.info(f"Directory {directory_name}, inner file(s) and content deleted succesfully.")
        else:
                logging.warning(f"The directory with this name {direct_name}, doesn't exists or already deleted.")
    elif question == "no":
        logging.warning(f"Skip.")
    
if __name__ == "__main__":
    # TODO, move this variable under main block
    directory_name = "Demo"
    file_name = "test.txt"
    content = "This is the content of the file."
    create_directory(directory_name)
    file_writing(file_name, content)
    file_reading(file_name,content)
    cleanup(directory_name)
# TODO, good job, structured and correct