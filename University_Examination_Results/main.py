import students.utilis as u

if __name__ == "__main__":
    direct_name = "ExaminationResults"
    f_name = "exam_results.xlsx"
    u.setup_logging()
    u.create_directory(direct_name)
    u.create_results_file(direct_name, f_name)
    u.analyze_results(direct_name, f_name)
    u.cleanup(direct_name)