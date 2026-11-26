import os
import shutil
import logging


new_folder = "Demo"
file_name = 'test.txt'
content = "This is the content of the file."


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s ___ [%(levelname)s] ____%(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    filename='my_log.log',
    filemode='a',
    encoding='utf-8'
)


def create_folder(new_folder, file_name, content):
    if not os.path.exists(new_folder):
       os.mkdir(new_folder)
       logging.info (f"Folder '{new_folder}' created successfully.")
    os.chdir(new_folder)
    with open(file_name, "w+", encoding="utf-8") as file:
        file.write(content)
        logging.info(f"File '{file_name}' created successfully.")

        
def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
         file.seek(0)
         data = file.read()
         print(data)


def delete_folder(new_folder):
    question  = input(f"Are you sure you want to delete the folder '{new_folder}'? (y/n): ")
    if question == "y":
     os.chdir("..")
     if os.path.exists(new_folder):
        shutil.rmtree(new_folder)
        print(f"Folder '{new_folder}' has been deleted.")
        logging.info(f"Folder '{new_folder}' has been deleted.")


if __name__ == "__main__":

    create_folder(new_folder, file_name, content)
    read_file(file_name)
    delete_folder(new_folder)
    logging.info