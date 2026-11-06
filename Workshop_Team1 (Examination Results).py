import os
import shutil
import logging
import pandas

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
        
    os.chdir(directory_name)
    logging.info(f"You are in {directory_name} directory")
      

def create_results_file(directory_name, file_name):
       df = pandas.DataFrame(data)
       df.to_excel("exam_results.xlsx", index=False) 
       logging.info(f"Data has been written to {file_name} Excel file.")
       
       

def analyze_results(directory_name, file_name):
    with open (file_name, "a+", encoding="utf-8") as file:
       read_df = pandas.read._excel(file_name)


    

def cleanup(directory_name):
 pass


if __name__ == "__main__":

  dir_name = "ExaminationResults" 
  excel_file_name = "exam_results.xlsx"
  data = {
 "Name": ["Anna", "David", "Emma", "Mark", "Sophia"],
 "Subject": ["Python", "Python", "Python", "Python", "Python"],
 "Score": [85, 92, 78, 88, 95]  
}

  setup_logging()
  logging.info("Program has started")

  create_directory(dir_name)
  file_path = os.path.join(dir_name, excel_file_name)
  create_results_file(dir_name, excel_file_name)
  analyze_results(dir_name, excel_file_name)


  