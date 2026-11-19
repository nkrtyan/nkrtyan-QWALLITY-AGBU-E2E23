import logging
import car_market as car
import logger_config as log

log.setup_logger()

logging.info("Program has started")

market = car.MyCar()
market.show_market()
market.search_car("BMW")
market.buy_car("Tesla", 2)

market.buy_car("BMW", 2)
market.search_car("BMW")  

logging.info(" Program finished")

