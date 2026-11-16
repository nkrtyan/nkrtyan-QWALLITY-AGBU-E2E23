import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO, 
        filename="app.log", 
        format="%(asctime)s - %(levelname)s: %(message)s", 
        filemode="w+",
        datefmt="%Y-%m-%d %H:%M:%S"
    )