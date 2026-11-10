import os
import shutil
import logging
import pandas
import data 

def setup_logging():
    
    logging.basicConfig(
        level=logging.INFO,      
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filemode='w+',
        filename='app.log',
        encoding='utf-8' 
    )


def create_directory(directory_name):
    if os.path.exists(directory_name):
       logging.info(f"Directory {directory_name} already exists.")
    else:
        os.mkdir(directory_name)
        logging.info(f"Directory {directory_name} is created")


def create_results_file(directory_name, file_name):
    file_path = os.path.join(directory_name,file_name)
    data_frame = pandas.DataFrame(data)
    data_frame.to_excel(file_path,index =False)
    logging.info(f"File {file_name} is created")


def analyze_results(directory_name, file_name):
    file_path = os.path.join(directory_name,file_name)
    data_frame = pandas.read_excel(file_path)

    students_count = len(data_frame)
    max_score = data_frame["Score"].max()
    min_score = data_frame["Score"].min()
    best_student = data_frame[data_frame["Score"]==max_score]["Name"].values[0]
    bad_student = data_frame[data_frame["Score"]==min_score]["Name"].values[0]

    logging.info(f"Number of examined students:{students_count}")
    logging.info(f"Best result:{best_student}:{max_score} ")
    logging.info(f"Best result:{bad_student}:{min_score}  ")


def cleanup(directory_name):
    user_input = input(f"Do you want ot remove the directory {directory_name} ? (yes/no): ").strip().lower()

    if user_input in ['yes','y']:
        if os.path.exists(directory_name):
            shutil.rmtree(directory_name)
            logging.info(f"Directory {directory_name} was deleted. ")
        else:
            logging.info(f"Directory {directory_name} does not exist. ")   
             