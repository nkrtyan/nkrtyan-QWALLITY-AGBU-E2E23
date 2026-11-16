
# from car_market_management.car_market import CarMarket, MyCar
# from car_market_management.logger_config import setup_logging
import logging
from car_market import CarMarket, MyCar
from logger_config import setup_logging

setup_logging()

car_car = CarMarket("BMW")
print(car_car.check_car_existence("BMW"))
car_car.show_market()
print("The original price of that brand", car_car.calculate_price("BMW"))
child_car = MyCar("BMW",2)
print(child_car.calculate_price("BMW"))
child_car.search_car("BMW")
child_car.buy_car("BMW", 1)