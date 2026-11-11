import logging
import os
import pandas
import shutil

# 1. Логирование (Logging)
def setup_logging():
    logging.basicConfig(
        filename='lesson_28/app.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

# 2. Создание директории (Create Directory)
os.makedirs('lesson_28', exist_ok=True)
directory_name = 'lesson_28/ExaminationResults'

def create_directry(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        logging.info('Directory was created')  


# 3. Создание Excel-файла (Create Excel File)
file_name = 'exam_results.xlsx'

data = {
        "Name": ["Anna", "David", "Emma", "Mark", "Sophia"],
        "Subject": ["Python", "Python", "Python", "Python", "Python"],
        "Score": [85, 92, 78, 88, 95]
        }

def create_results_file(directory_name, file_name):
        df = pandas.DataFrame(data)
        df.to_excel(f'{directory_name}/{file_name}')
        logging.info('File was created')    


# 4. Анализ результатов экзамена (Analyze Exam Results)
def analyze_results(directory_name, file_name):
    data = pandas.read_excel(f'{directory_name}/{file_name}')
    
    students_count = len(data)
    logging.info(f'Number of examined students: {students_count}')    

    max_result = data['Score'].max()
    min_result = data['Score'].min()

    best_students = data.loc[data["Score"] == max_result , 'Name'].tolist()
    worst_students = data.loc[data["Score"] == min_result, 'Name'].tolist()
    logging.info(f'Best result: {','.join(best_students)} - {max_result}')
    logging.info(f'Lowest result: {','.join(worst_students)} - {min_result}')

# 5. Очистка (Cleanup)
def cleanup(directory_name):
    if os.path.exists(directory_name):
         question= input('Clear directory?(Yes/No)')
         if question == 'Yes':
            shutil.rmtree(directory_name)
            logging.info('Directory was deleted')
         else:
              logging.info('Directory was not deleted')
    else:
        logging.info('Directory does not exist')
         


if __name__ == "__main__":
     setup_logging()
     create_directry(directory_name)
     create_results_file(directory_name, file_name)
     analyze_results(directory_name,file_name )
     cleanup(directory_name)


