import os
import logging
import shutil
import pandas as pd

data = {
 "Name": ["Anna", "David", "Emma", "Mark", "Sophia"],
 "Subject": ["Python", "Python", "Python", "Python", "Python"],
 "Score": [85, 92, 78, 88, 95]
}

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s ___ [%(levelname)s] ____ %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S',
        filename='app.log',
        filemode='a',
        encoding='utf-8'
    )



def create_directory(directory_name):
  if not os.path.exists(directory_name):
    os.mkdir(directory_name)
    # os.chdir(directory_name)
    logging.info(f"Directory '{directory_name}' created successfully.")
  else:
    logging.info(f"Directory '{directory_name}' already exists.")

    
def create_results_file(directory_name, file_name):
    if not os.path.exists(directory_name):
           os.mkdir(directory_name)
           logging.info (f"Folder '{directory_name}' created successfully.")

    df = pd.DataFrame(data)

    file_path = os.path.join(directory_name, file_name)

    df.to_excel(file_path, index=False)

    logging.info(f"Results file '{file_name}' created successfully.")
 

def analyze_results(directory_name, file_name):
   file_path = os.path.join(directory_name, file_name)
   
   read_df = pd.read_excel(file_path, usecols=["Name", "Score"])


   students_count = len(read_df )
   highest_score = read_df["Score"].max()

   lowest_score = read_df["Score"].min()
   best_student = read_df.loc[read_df["Score"] == highest_score, "Name"].iloc[0]
   lowest_student = read_df.loc[read_df["Score"] == lowest_score, "Name"].iloc[0]
   
   logging.info(f"Number of examined students: {students_count}")
   logging.info(f"Best result: {best_student} - {highest_score}")
   logging.info(f"Lowest result: {lowest_student} - {lowest_score}")
   print(read_df)
  

def cleanup(directory_name):
    question  = input(f"Are you sure you want to delete the folder '{directory_name}'? (y/n): ")
    if question.lower() == "y":
    #    os.chdir("..")
       if os.path.exists(directory_name):
        shutil.rmtree(directory_name)
        print(f"Folder '{directory_name}' has been deleted.")
        logging.info(f"Folder '{directory_name}' has been deleted.")
        print(f"Folder '{directory_name}' has been deleted.")


if __name__ == "__main__":

     setup_logging()
     
     directory_name = "ExaminationResults"
     file_name = "exam_results.xlsx"
     create_directory(directory_name)
     create_results_file(directory_name, file_name)
     analyze_results(directory_name, file_name)
     cleanup(directory_name)

