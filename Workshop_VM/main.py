import logging
from . import utils

dir_name = "ExaminationResults"
file_name = "exam_results.xlsx"


utils.setup_logging()
utils.create_directory(dir_name)
utils.create_file_results(dir_name, file_name)
utils.analyze_results(dir_name, file_name)
utils.clean_up(dir_name)