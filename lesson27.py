import os
import shutil
import logging

logging.basicConfig(
   level=logging.INFO,  # TODO, use 4 spaces for indentation in all lines
   format="%(asctime)s - %(levelname)s: %(message)s",
   datefmt="%Y-%m-%d %H:%M:%S"
)


dir_name = "Demo" # TODO, move under main block

def create_directory():  # TODO, pass dir_name as argument to all functions, keep 2 empty lines between functions
   if not os.path.exists(dir_name):
      os.mkdir(dir_name)
      logging.info(f"Directory '{dir_name}' is ready.")

def write_file():
   file_path = os.path.join(dir_name, "test.txt")
   with open(file_path, "w+") as file:
      file.write("This is the content of the file.") # TODO, keep content as an argument and pass to function
      logging.info("File 'test.txt' created and written.")

def read_file(): # TODO, should take as an argument dirname and file name 
   file_path = os.path.join(dir_name, "test.txt")
   with open(file_path, "r") as file:
      content = file.read()
      print("File content:", content)
      logging.info("File content read successfully.")

def cleanup():
   answer = input("Do you want to delete the Demo directory and its contents? (yes/no): ")
   if answer == "yes": 
        # TODO, need to check if dir exists after delete it
        shutil.rmtree(dir_name)
        logging.info(f"Directory '{dir_name}' deleted.")
   else: 
        logging.info("Cleanup cancelled. Directory 'Demo' was not deleted.")  # TODO, use logging.warning here, use dir_name instead of 'Demo' text in all places


if __name__ == "__main__":
   #TODO, keep variable names here 
   create_directory()
   write_file()
   read_file()
   cleanup()

# Nel, working code