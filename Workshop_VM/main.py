import logging
import utils
import config as log

log.setup_logging()


dir_name = "ExaminationResults"
file_name = "exam_results.xlsx"

utils.create_directory(dir_name)
utils.create_file_results(dir_name, file_name)
utils.analyze_results(dir_name, file_name)
utils.clean_up(dir_name)