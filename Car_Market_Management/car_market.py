import logging
import logger_config

class CarMarket:
    car_market_data = {
        "BMW": {
            "price": 50000,
            "Stock": 5,
        },
        "Toyota": {
            "price": 30000,
            "Stock": 5,
        },
        "Ford": {
            "price": 35000,
            "Stock": 5,
        },
        "Honda": {
            "price": 32000,
            "Stock": 5,
        },

    }
    def __init__(self, brand):
        self.brand = brand

    def check_car_existence(self, brand):
        if brand in self.car_market_data:
            logging.info(f"{self.brand} is exist")
            print(f"car brand  - {self.brand}")


    def show_market(self):
        for brand, index in self.car_market_data.items():
# info

        print(f"brand -{self.brand}")

#     def calculate_price(self, brand):
#         pass


# class MyCar(CarMarket):
#     def __init__(self, brand, quantity):
#         CarMarket.__init__(self, brand)

#     def calculate_price(self, brand):
    # override

     
#     def search_car(self, brand):
# isesist 


#     def buy_car(self, brand, quantity):
# stock
# if is exist in stock -1
# else if not enough


