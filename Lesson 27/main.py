import logging
import os 
from utils import create_directory, create_file, delete_directory, read_file

directory_name = "demo"
file_path = os.path.join(directory_name, "test.txt")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

if __name__ == "__main__":
    create_directory()
    create_file()
    read_file()
    delete_directory()

    logging.info("Directory and file operations completed successfully.")