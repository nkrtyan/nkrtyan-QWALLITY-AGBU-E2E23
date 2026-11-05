import os
import shutil
import logging

logging.basicConfig(
   level=logging.INFO,
   format="%(asctime)s - %(levelname)s: %(message)s",
   datefmt="%Y-%m-%d %H:%M:%S"
)


dir_name = "Demo"

def create_directory():
   if not os.path.exists(dir_name):
       os.mkdir(dir_name)
logging.info(f"Directory '{dir_name}' is ready.")

def write_file():
   file_path = os.path.join(dir_name, "test.txt")
   with open(file_path, "w+") as file:
       file.write("This is the content of the file.")
logging.info("File 'test.txt' created and written.")

def read_file():
   file_path = os.path.join(dir_name, "test.txt")
   with open(file_path, "r") as file:
       content = file.read()
       print("File content:", content)
logging.info("File content read successfully.")

def cleanup():
   answer = input("Do you want to delete the Demo directory and its contents? (yes/no): ")
   if answer == "yes":
        shutil.rmtree(dir_name)
        logging.info(f"Directory '{dir_name}' deleted.")
   else: 
        logging.info("Cleanup cancelled. Directory 'Demo' was not deleted.")


if __name__ == "__main__":
   create_directory()
   write_file()
   read_file()
   cleanup()