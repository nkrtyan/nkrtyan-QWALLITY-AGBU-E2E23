import logging
     
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s ___ [%(levelname)s] ____ %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S',
        filename='Car.log',
        filemode='w+',
        encoding='utf-8'
    ) 