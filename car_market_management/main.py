import logger_config
from car_market import MyCar

car_brand = input("Enter your car brand: ")
car_obj = MyCar(car_brand, discount=20)

car_obj.show_market()
car_obj.search_car(car_brand)
car_obj.buy_car(car_brand, quantity=2)