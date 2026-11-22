import logging

class CarMarket:

    def __init__(self, brand):
        self.brand = brand


    car_market_data = {
    "BMW": {
        "price": 50000,
        "stock": 5
    },
    "Toyota": {
        "price": 30000,
        "stock": 5
    },
    "Ford": {
        "price": 35000,
        "stock": 5
    },
    "Honda": {
        "price": 32000,
        "stock": 5
    },
    "Kia": {
        "price": 34000,
        "stock": 5
    },
    "BYD Sealion": {
        "price": 40000,
        "stock": 5
    },
    "Bugatti": {
        "price": 2500000,
        "stock": 5
    },
    "Audi": {
        "price": 55000,
        "stock": 5
    },
    "Mercedes-Benz": {
        "price": 60000,
        "stock": 5
    },
    "Hyundai": {
        "price": 27000,
        "stock": 5
    }
}
    

    def check_car_existence(self,brand):
        return brand in self.car_market_data

    def show_market(self):
        for brand in self.car_market_data:
            logging.info(f"{brand} - Price: {self.car_market_data[brand]['price']}, Stock: {self.car_market_data[brand]['stock']}")
    
    def calculate_price(self,brand):
        if self.check_car_existence(brand):
            return self.car_market_data[brand]['price']
        else:
            return None
        

class MyCar(CarMarket):
    def __init__(self, brand, discount):
        super().__init__(brand)
        self.discount = discount
        
    def calculate_price(self,brand):
        if not self.check_car_existence(brand):
           return None
        if brand == "BMW":
            return self.car_market_data[brand]['price'] *  (1 - self.discount / 100)
        else:
            return self.car_market_data[brand]['price']
        
    def search_car(self, brand):
        if not self.check_car_existence(brand):
           logging.error(f"{brand} was not found.")
        else:
            logging.info(f"{brand} was found successfully.")
            logging.info(f"Brand: {brand}")
            logging.info(f"Original price: {self.car_market_data[brand]['price']}")
            logging.info(f"Final price: {self.calculate_price(brand)}")
            logging.info(f"Available stock: {self.car_market_data[brand]['stock']}")

    def buy_car(self, brand, quantity):
        if not self.check_car_existence(brand):
            logging.error("Car was not found.")
            return
        elif quantity <= 0:
            logging.error("Invalid quantity.") 
            return
        elif quantity > self.car_market_data[brand]['stock']:
            logging.error("There is not a sufficient quantity.")
            return
        

        total_price = self.calculate_price(brand) * quantity
        self.car_market_data[brand]['stock'] -= quantity
        logging.info(f"Purchased quantity: {quantity}")
        logging.info(f"Total price: {total_price}")
        logging.info(f"Remaining stock: {self.car_market_data[brand]['stock']}")