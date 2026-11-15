import logging
import car_market as car
import logger_config as log

log.logging_function()

logging.info("Program has started")

market = car.MyCar()

market.show_market()
market.search_car("BMW")
market.buy_car("Tesla", 2)

logging.info(" Program finished")




