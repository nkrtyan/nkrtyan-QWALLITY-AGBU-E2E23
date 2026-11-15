import logging

def logging_function():

    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s------%(levelname)s------%(message)s",
        filename = "car_market.log",
        filemode = "a+"
    )


    