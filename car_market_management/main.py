import logging
from logger_config import setup_logger   
import car_market 


my_car = car_market.MyCar("BMW", 2)

my_car.show_market()

my_car.search_car("BMW")       
my_car.search_car("Tesla")      

my_car.calculate_price("BMW")   
my_car.calculate_price("Toyota") 

my_car.buy_car("BMW", 2)      
my_car.buy_car("Toyota", 10)    
my_car.buy_car("Honda", 0)