import os
import shutil
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%d-%m-%Y',
    filename='mylog.log',
    filemode='a+',
)


dir_name = "Demo"
file_name = "test.txt"


def create_direct(dir_name):

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def create_write_file(file_name, dir_name):

    os.chdir(dir_name)
    with open(file_name, "a+") as file:
        file.write("This is the content of the file.")


def read_file(file_name):
    with open(file_name, "a+") as file:
        file.seek(0)
        mytext = file.read()
        print(mytext)


def cleanup_direct(dir_name):
    if os.path.exists(dir_name):
        question = input("Do you want to delete directory yes or no: ")
        if question == "yes":
            os.chdir("..")
            shutil.rmtree(dir_name)
            logging.info("That directory has been deleted.")
        elif question == "no":
            logging.info("The directory was not deleted.")


def print_separator():
    print()


if __name__ == "__main__":

    create_direct(dir_name)
    create_write_file(file_name, dir_name)
    read_file(file_name)

    print_separator()
    cleanup_direct(dir_name)