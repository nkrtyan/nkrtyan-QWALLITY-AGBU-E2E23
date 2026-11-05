import os
import shutil
import logging
# TODO, move logging.basicConfig here, after imports

dir_name="Demo"  # TODO, add spaces around "=" in all lines
file_name="text.txt"
content="This is the content of the file."

# - Directory Creation
def created_directory (dir_name, file_name, content):  # TODO, rename to create_directory, remove space before "(", split into 3 functions: create dir, write file, read file
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    file_path=os.path.join(dir_name, file_name)
    with open(file_path, "w+") as f: #-File Creation and Writing:
        f.write(content)
        f.seek(0)
        dir_read=f.read() # - File Reading: 
        print(dir_read)

# TODO, keep 2 empty lines between functions
def delete_dir(dir_name): # - Cleanup: 
    if os.path.exists(dir_name):
        answer=input("Do you want to delete the directory? (Y/N): ")
        if answer=="Y":
            shutil.rmtree(dir_name)

# TODO, mobe the logging configuration to up
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s ---- %(levelname)s ----- %(message)s",
    datefmt="%d-%m-%Y",
    filename="les_27.log",
    filemode="a+",
    encoding="utf-8")


if __name__=="__main__":
    # TODO, you should have few function calls, dir creation, file wrinting, reading, cleanup
    created_directory(dir_name, file_name, content)  
    delete_dir(dir_name)  
    logging.info("Directory created and deleted successfully.")  # TODO, this is logged even if answer is "N", log only when directory is deleted
# TODO, remove extra empty lines at the end of file


