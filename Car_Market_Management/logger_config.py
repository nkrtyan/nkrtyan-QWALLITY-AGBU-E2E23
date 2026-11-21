import logging

def info_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(message)s', 
        datefmt='%Y-%m-%d %H:%M:%S', 
        filename='Car_Market_Management/car_market.log',
        filemode='a+', 
        encoding='utf-8' 
    )