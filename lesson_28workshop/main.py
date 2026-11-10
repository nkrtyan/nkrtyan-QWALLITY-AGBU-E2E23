from data import data
import utils

if __name__ == "__main__":
    dir_name = "ExaminationResults"
    file_name = "exam_results.xlsx"

    utils.setup_logging()
    utils.create_directory(dir_name)
    utils.create_results_file(dir_name, file_name, data)
    utils.analyze_results(dir_name, file_name)
    utils.cleanup(dir_name)
    