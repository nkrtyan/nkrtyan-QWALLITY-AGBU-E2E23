from .data import data

import os
import shutil
import logging
import pandas as pd

def setup_logging():
    logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S', 
    filename='exam_log.log',
    filemode='a+', 
    encoding='utf-8' 
    )


def create_directory(directory_name):
    logging.info("--- The Program Starts ---")
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
        logging.info(f"The directory with this names {directory_name} was created succesfully.")
    else:
        logging.info(f"The directory with this name {directory_name}, already exists.")


def create_results_file(directory_name, file_name):
    df_path = os.path.join(directory_name, file_name)
    df = pd.DataFrame(data)
    df.index = range(1,len(df) + 1)
    df.index.name = "Id"
    df.to_excel(df_path, index=True)
    logging.info(f"The File with this {file_name} name, inside {directory_name} directory was created succesfully.")


def analyze_results(directory_name, file_name):
    df_path = os.path.join(directory_name, file_name)
    read_df = pd.read_excel(df_path)
    analysis_df = read_df[['Name', 'Score']]
    total_students = len(analysis_df)
    highest_score = analysis_df['Score'].max()
    lowest_score = analysis_df['Score'].min()
    highest_students = []
    lowest_students = []
    for index, row in analysis_df.iterrows():
        if row['Score'] == highest_score:
           highest_students.append(row['Name'])
        elif row['Score'] == lowest_score:
           lowest_students.append(row['Name'])
    highest_names = ", ".join(highest_students)
    lowest_names = ", ".join(lowest_students)
    logging.info(f"{file_name} is created and read. Content: \n{read_df}")
    logging.info("--- Exam Results Analysis ---")
    logging.info(f"Total students who took the exam: {total_students}")
    logging.info(f"Highest score: {highest_names} - {highest_score} ")
    logging.info(f"Lowest score: {lowest_names} - {lowest_score}")


def cleanup(directory_name):
    question = input("Do you want to delete direction? (yes or no): ")
    if question == "yes":
        # os.chdir("..")
        if os.path.exists(directory_name):
            shutil.rmtree(directory_name)
            logging.info(f"Directory {directory_name}, inner file(s) and content deleted succesfully.")
        else:
            logging.warning(f"The directory with this name {directory_name}, doesn't exists or already deleted.")
    elif question == "no":
        logging.warning(f"Skip.")
    logging.info("--- The programme finished ---")