import os
import shutil
import logging
import pandas


data = {
          "Name": ["Anna", "David", "Emma", "Mark", "Sophia"],
          "Subject": ["Python", "Python", "Python", "Python", "Python"],
          "Score": [85, 92, 78, 88, 95] 
}

def setup_logging():
    logging.basicConfig(

    format="%(asctime)s--------%(levelname)s--------%(message)s",
    level = logging.INFO,
    filename = "app.log" 

    ) 


def create_directory(directory_name):
    if not os.path.exists(directory_name):
      os.mkdir(directory_name)
      logging.info (f"Directory {directory_name} created")
    else:
      logging.info(f"Directory {directory_name} already exists")  
      
      

def create_results_file(file_path):
  df = pandas.DataFrame(data)
  df.to_excel(file_path, index=False) 
  logging.info(f"Data has been written to {file_path} Excel file.")

       
def analyze_results(file_path):
  read_df = pandas.read_excel(file_path)
  names = read_df['Name']
  scores = read_df['Score']

  highest_score = scores.max()
  lowest_score = scores.min()
  logging.info(f'Number of examined students: {len(names)}')
  for i in range(len(names)):
    if scores[i] == highest_score:
      logging.info(f"Best result: {names[i]} - {scores[i]}")

    if scores[i] == lowest_score:
      logging.info(f"Lowest result: {names[i]} - {scores[i]}")   



def cleanup(directory_name):
  question  = input(f"Are you sure you want to delete the folder '{directory_name}'? type Yes/No: ")
  if question.lower() == "yes":
    if os.path.exists(directory_name):
      shutil.rmtree(directory_name)
      print(f"Folder '{directory_name}' has been deleted.")
      logging.info(f"Folder '{directory_name}' has been deleted.")
    else: 
      logging.info(f"Directory '{directory_name}' doesn't exist")  
  else:
    logging.info(f"User does not want to delete the directory")      


if __name__ == "__main__":

  dir_name = "ExaminationResults" 
  excel_file_name = "exam_results.xlsx"

  setup_logging()
  logging.info("Program has started")

  create_directory(dir_name)
  file_path = os.path.join(dir_name, excel_file_name)
  create_results_file(file_path)
  analyze_results(file_path)
  cleanup(dir_name)



  