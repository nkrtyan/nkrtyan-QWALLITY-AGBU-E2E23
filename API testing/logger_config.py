import logging

def info_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(message)s', 
        datefmt='%Y-%m-%d %H:%M:%S', 
        filename='API testing/api_l.log',
        filemode='a+', 
        encoding='utf-8' 
    )