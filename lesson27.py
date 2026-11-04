import os
import shutil
import logging

direct_name = "Demo"
file_name = "test.txt"

def create_direct(direct_name):
    if not os.path.exists(direct_name):
        os.mkdir(direct_name)



def create_write_file(file_name, direct_name):
    os.chdir(direct_name)
    with open(file_name, "a+") as file:
        file.write("This is the content of the file.")



def read_file(file_name):
    with open(file_name, "a+") as file:
        file.seek(0)
        mytext = file.read()
        print(mytext)


def cleanup_direct(direct_name):
    question = input("Do you want to delete directory yes or no: ")
    if question == "yes":
        os.chdir("..")
        if os.path.exists(direct_name):
            shutil.rmtree(direct_name)
    elif question == "no":
        print("The directory was not deleted.")


def print_separator():
    print()




logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%d-%m-%Y',
    filename='mylog.log',
    filemode='a+',
)


if __name__ == "__main__":
    create_direct(direct_name)
    create_write_file(file_name, direct_name)
    read_file(file_name)
    print_separator()
    cleanup_direct(direct_name)
    os.chdir("..")
    if not os.path.exists(direct_name):
        logging.info("That directory has been deleted.")
    else:
        logging.error("That directory has not been deleted.")


