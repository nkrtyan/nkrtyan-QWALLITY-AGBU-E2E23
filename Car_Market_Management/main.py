import logging
import car_market as car
import logger_config as log

#FIX call path coverage

log.setup_logger()

logging.info("Program has started")

market = car.CarMarket("BMW")

market.check_car_existence("BMW")
market.show_market()
market.calculate_price("BMW")

market_child = car.MyCar("Tesla", 1)

market_child.calculate_price("Ford")
market_child.search_car("Bugatti")
market_child.buy_car("BMW", 2)

logging.info(" Program finished") 




