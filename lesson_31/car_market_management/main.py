from car_market import CarMarket
from car_market import MyCar
from logger_config import logger

car = CarMarket('BMW')
print(car.check_car_existence('Ford'))
print(car.show_market())
print(car.calculate_price('Toyota'))

car2 = MyCar('Audi')
print(car2.calculate_price2('BMW', 0.8))
print(car2.search_car('Toyota'))
print(car2.buy_car('Toyota', 2))
print(car2.buy_car('Toyota', 4))