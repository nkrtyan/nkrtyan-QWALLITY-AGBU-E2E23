import logging


class CarMarket:
    
    car_market = {
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
    
    def __init__(self, brand):
        self.brand = brand
    
    def check_car_existence(self):
        return self.brand in self.car_market
    
    
    def show_market(self):
        logging.info("\n========== CAR MARKET ==========")

        for brand, details in self.car_market.items():
            logging.info(
                f"Brand: {brand} | "
                f"Price: {details['price']} | "
                f"Stock: {details['stock']}"
            )
    
    
    def calculate_price(self):
        if self.check_car_existence():
            return self.car_market[self.brand]['price']
        else:
            logging.info(f"Car {self.brand} is unavailable for price calculation.")
            return None
        
        

class MyCar(CarMarket):
    discount = 0.80
    
    def __init__(self, brand, quantity):
        super().__init__(brand)
        self.quantity = quantity
        
        
    def calculate_price(self):
        original_price = super().calculate_price()
        
        if original_price is None:
            logging.info(f"{original_price} is unavailable. ")
            return None
        elif self.brand == "BMW":
            return original_price * self.discount
        else:
            return original_price
        
        
    def search_car(self):
        if self.check_car_existence():
            car = self.car_market[self.brand]

            logging.info(f"\nCar found: {self.brand}")
            logging.info(f"Original price: ${car['price']}")
            logging.info(f"Final price: ${self.calculate_price()}")
            logging.info(f"Available stock: {car['stock']}")
            logging.info(f"Successful car search: {self.brand}")
        else:
            logging.info(f"Unsuccessful search: {self.brand} is unavailable.")
       
            
            
    def buy_car(self):
        logging.info("\n Purchased Car Info: ")
        
        if not self.check_car_existence():
            logging.error(f"Car {self.brand} is unavailable.")
            return None
        elif type(self.quantity) != int or self.quantity <= 0:
            logging.error(f"Purchase failed: Invalid quantity {self.quantity}")
            return None
        elif self.quantity > self.car_market[self.brand]['stock']:
            logging.error(f"Insufficient stock for {self.brand}. Requested: {self.quantity}")
            return None
        else:
            price = self.calculate_price()
            total_price = price * self.quantity
            self.car_market[self.brand]['stock'] -= self.quantity

            logging.info("\nPurchase successful!")
            logging.info(f"Car: {self.brand}")
            logging.info(f"Quantity: {self.quantity}")
            logging.info(f"Price per car: ${price}")
            logging.info(f"Total price: ${total_price}")
            logging.info(f"Remaining stock: {self.car_market[self.brand]['stock']}")
            return total_price
        
