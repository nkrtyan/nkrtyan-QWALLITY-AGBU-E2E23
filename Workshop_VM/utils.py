from Workshop_VM import data as data
import os
import shutil
import pandas
import logging
from Workshop_VM import config as config

def setup_logging():
    config.config

def create_directory(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        logging.info(f"Directory {dir_name} is created.")
    else:
        logging.info(f"The {dir_name} have already exist.")

def create_file_results(dir_name, file_name):
    file_path = os.path.join(dir_name, file_name)
    df = pandas.DataFrame(data.data)
    df.to_excel(file_path, index=False)
    logging.info(f"{file_path} is created.")

def analyze_results(dir_name, file_name):
    file_path = os.path.join(dir_name, file_name)
    df = pandas.read_excel(file_path)
    name_score = df[["Name", "Score"]]
    count_students = len(name_score)
    high_score = df["Score"].max()
    low_score = df["Score"].min()
    
    for _, n in name_score.iterrows():
        if n["Score"] == high_score:
            print(f"The highest score is : {high_score} and the student is {n['Name']}.")
        elif n["Score"] == low_score:
            print(f"The lowest score is : {low_score} and the student is {n['Name']}.")

    logging.info(f"The count of students is {count_students}.")
    logging.info(f"The highest score is : {high_score}.")
    logging.info(f"The lowest score is {low_score}.")

def clean_up(dir_name):
    answer = input(f"Do you want to delete the '{dir_name}' directory and its contents? (yes/no): ")

    if answer == "yes":
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            logging.info(f"Directory '{dir_name}' deleted.")
        else:
            logging.warning(f"Directory '{dir_name}' does not exist.")
    else:
      logging.warning(f"Cleanup cancelled. Directory '{dir_name}' was not deleted.")
