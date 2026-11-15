import logging
from logger_config import setup_logger

setup_logger()

class CarMarket:
    cars = {
        "BMW": {"price": 50000, "stock": 5},
        "Toyota": {"price": 30000, "stock": 5},
        "Ford": {"price": 35000, "stock": 5},
        "Honda": {"price": 32000, "stock": 5},
        "Kia": {"price": 34000, "stock": 5},
        "BYD Sealion": {"price": 40000, "stock": 5},
        "Bugatti": {"price": 2500000, "stock": 5},
        "Audi": {"price": 55000, "stock": 5},
        "Mercedes-Benz": {"price": 60000, "stock": 5},
        "Hyundai": {"price": 27000, "stock": 5}
    }

    def __init__(self,brand = None):
        self.brand = brand

    def check_car_existence ( self,brand):
        if brand in self.cars:
            logging.info(f"Car brand '{brand}' exists.")
            return True
        else:
            logging.error(f"Car brand '{brand}' does not exist.")
            return False

    def show_market(self):
        for brand,details in self.cars.items():
            logging.info(f"{brand} - {details}")

    def calculate_price(self,brand):
        if self.check_car_existence(brand):
            logging.info(f"price: {self.cars[brand]["price"]}") 

class MyCar(CarMarket):

    def __init__(self,brand = None,quantity =None):
        super().__init__(brand)
        self.quantity = quantity

    def calculate_price(self, brand):
        original_price = super().calculate_price(brand)   

        if original_price is None:
            return None
         
        if brand.strip().upper() == "BMW":
            discounted_price = original_price * 0.8
            logging.info(f"BMW price with 20% discount is: {discounted_price}")
            return discounted_price
        
        logging.info(original_price)
        return original_price

    def search_car(self,brand):
        if self.check_car_existence(brand):
            original_price = super().calculate_price(brand)
            final_price = self.calculate_price(brand)
            stock_quantity = self.cars[brand]["stock"]
            logging.info((f"Successfully searched for car: '{brand}'. Stock : {stock_quantity}."))

    def buy_car(self,brand,quantity):
        if self.check_car_existence(brand):
            logging.info(f"Car brand '{brand}' exists.")
            return 1
        if quantity <= 0 :
            logging.info(f"invalid {quantity}")
            return 1
        
        current_stock = self.cars[brand]["stock"]
        if quantity > current_stock:
            logging.info(f"Insufficient stock for {brand}")
            return 1

        unit_price = self.calculate_price(brand)
        total_price = unit_price * quantity
        self.cars[brand]["stock"] -= quantity  

        logging.info(f"unit final price : {unit_price} , total cost : {total_price}, stock: {self.cars[brand]["stock"]}")  
