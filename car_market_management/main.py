import logging
import car_market as car
import logger_config as log

log.setup_logger()

logging.info("Program has started")

logging.info("----- SCENARIO 1: Show market -----")
car.MyCar("BMW", 1).show_market()
logging.info("----- SCENARIO 2: Search car WITH discount -----")
car.MyCar("BMW", 1).search_car()
logging.info("----- SCENARIO 3: Search car that does not exist -----")
car.MyCar("Tesla", 2).search_car()
logging.info("----- SCENARIO 4: Buy car successfully -----")
car.MyCar("BMW", 2).buy_car()
logging.info("----- SCENARIO 5: Buy with invalid quantity -----")
car.MyCar("Audi", 0).buy_car()
logging.info("----- SCENARIO 6: Buy more than in stock -----")
car.MyCar("Bugatti", 10).buy_car()

logging.info(" Program finished")

