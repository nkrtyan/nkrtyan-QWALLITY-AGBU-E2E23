from car_market import CarMarket, MyCar
from logger_config import info_logging 
import logging

info_logging()

logging.info("----Program Starts----")
logging.info("1. Check whether the car brand exists in the market. " \
"Return True or False")
car_market_obj = CarMarket("Bugatti")
car_market_obj.check_car_existence("Bugatti")
logging.info("2. Display all available car brands, prices, and stock quantities.")
car_market_obj.show_market()
logging.info("3. Return the original price of the selected car. Return" \
"None if the brand does not exist.")
car_market_obj.calculate_price("BMW")

my_car_obj = MyCar("BMW")
logging.info("4. Override the parent method. Apply a 20% discount for BMW. " \
"Return the original price for other brands.")
my_car_obj.calculate_price("Ford")
logging.info("5. Search for a car and display its brand, original price, " \
"final price, and available stock. Display a message if the car does not exist.")
my_car_obj.search_car("asd")
logging.info("6. Check availability and stock, calculate the total " \
"price, and reduce stock after a successful purchase. Reject invalid " \
"quantities or insufficient stock without changing the stock.")
my_car_obj.buy_car("Bugatti", 0)
logging.info("----Program Finished----")