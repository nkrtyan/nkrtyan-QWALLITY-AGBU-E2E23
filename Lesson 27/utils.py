import os
import shutil
import logging

directory_name = "demo"
file_path = os.path.join(directory_name, "test.txt")


def create_directory():
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    else:
        logging.info(f"Directory '{directory_name}' already exists.")


def create_file():
    with open(file_path, "w") as file:
        file.write("This is a test file.")

    logging.info(f"File '{file_path}' created successfully.")


def read_file():
    with open(file_path, "r") as file:
        content = file.read()

    print(f"Content of '{file_path}': {content}")
    logging.info(f"Content of '{file_path}': {content}")


def delete_directory():
    if os.path.exists(directory_name):
        confirmation = input(
            f"Are you sure you want to delete the directory '{directory_name}' and its contents? (y/n): "
        )

        if confirmation.lower() == "y":
            shutil.rmtree(directory_name)
            logging.info("Directory and its contents deleted successfully.")
        else:
            logging.info("Deletion canceled.")