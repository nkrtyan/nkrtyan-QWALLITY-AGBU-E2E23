import os
import shutil
import logging

logging.basicConfig(
    level=logging.DEBUG,      
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='my_log.log',
    filemode='a',  
    encoding='utf-8' 
)

def create_directory(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        logging.info(f"Directory '{dir_name}' created successfully.")
    else:
        logging.warning(f"Directory '{dir_name}' already exists.")

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        logging.info(f"File '{file_path}' created and text written successfully.")

def read_file(file_path):
    if not os.path.exists(file_path):
        logging.error(f"File '{file_path}' does not exist.")
        return # TODO, what you return here?
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
        print(f"Data read from file:\n{data}")
        logging.debug(f"Data read from file: {data.strip()}")

def clean_up(dir_name):
    if os.path.exists(dir_name):
        response = input(f"Are you sure you want to delete '{dir_name}' and all its contents? (y/n): ").strip().lower()
        
        if response in ('y', 'yes'):
            shutil.rmtree(dir_name)
            logging.info(f"Directory '{dir_name}' and its contents removed successfully.")
            print("Directory deleted successfully.")
        else:
            logging.info(f"Deletion of directory '{dir_name}' was cancelled by the user.")
            print("Deletion cancelled.")
    else:
        logging.warning(f"Directory '{dir_name}' does not exist.")
        print(f"Directory '{dir_name}' does not exist.")

if __name__ == "__main__":
    my_directory = "Demo"
    my_file_name = "test.txt"
    file_path = os.path.join(my_directory, my_file_name)
    my_text = "This is the content of the file.\n"

    print("Program started...")
    
    create_directory(my_directory)
    write_file(file_path, my_text)
    read_file(file_path)
    clean_up(my_directory)
    
    print("Program finished. Check 'my_log.log'.")
# TODO, the code is clean and structured, good for you