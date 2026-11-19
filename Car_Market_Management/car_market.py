import logging
class CarMarket:
    
    car_market = {
        "BMW": 
        {
           "Price": 50000, "Stock": 5
        },
        "Toyota": 
        {
           "Price": 30000, "Stock": 5
        },
        "Ford": 
        {
           "Price": 35000, "Stock": 5
        },
        "Honda":
        {
           "Price": 32000, "Stock": 5
        },
        "Kia":
        {
           "Price": 34000, "Stock": 5
        },
        "BYD Sealion":
        {
           "Price": 40000, "Stock": 5
        },
        "Bugatti":
        {
           "Price": 2500000, "Stock": 5
        },
        "Audi":
        {
           "Price": 55000, "Stock": 5
        },
        "Mercedes-Benz":
        {
           "Price": 60000, "Stock": 5
        },
        "Hyundai":
        {
           "Price": 27000, "Stock": 5
        }
    }

        #TODO init, 
    def check_car_existence(self, brand):
        if brand in self.car_market:
            return True
        #TODO logs
        else:
            return False
        #TODO logs
    
    
    def show_market(self):
        print("\n========== CAR MARKET ==========")

        for brand, details in self.car_market.items():
            print(
                f"Brand: {brand} | "
                f"Price: {details['Price']} | "
                f"Stock: {details['Stock']}"
            )
            logging.info("Car Market shows successfully")  # TODO (brand,price,stock)
    
    
    def calculate_price(self, brand):
        if self.check_car_existence(brand):
            return self.car_market[brand]['Price']
        else:
            logging.info("Car {brand} is unavailable for price calculation.")
            return None
        

class MyCar(CarMarket):
        
    def calculate_price(self, brand):
        original_price = super().calculate_price(brand)
        
        if original_price is None:
            logging.info("{original_price} is unavailable. ")
            return None
        
        elif brand == "BMW":
            return original_price * 0.80 #TODO discount, logs
        else:
            return original_price
        
        
    def search_car(self, brand):
        if self.check_car_existence(brand):
            logging.info("Unsuccessful search: {brand} is unavailable.")
        else:
            original_price = super().calculate_price(brand)
            final_price = self.calculate_price(brand)
            stock = self.car_market[brand]['Stock']

            print(f"\nCar found: {brand}")
            print(f"Original price: ${original_price}")
            print(f"Final price: ${final_price}")
            print(f"Available stock: {stock}")
            
            logging.info(f"Successful search: {brand}")

            # if brand == "BMW":
            #     print("Discount applied: 20%") # TODO replace in calculate function

            logging.info("Successful car search: {brand}")
            
    
    def buy_car(self, brand, quantity):
        print("\n Purchased Car Info: ")
        
        if not self.check_car_existence(brand):
            print(f"{brand} is not available.")
            logging.info(f"Car {brand} is unavailable.")
            return

        if type(quantity) != int or quantity <= 0:
            print("Invalid quantity. Please enter a positive number. \n")
            logging.error(f"Purchase failed: Invalid quantity {quantity}")
            return
        
        elif quantity > self.car_market[brand]['Stock']:
            print("Insufficient stock!")
            logging.info(f"Insufficient stock for {brand}. Requested: {quantity}")
            return

        price = self.calculate_price(brand)
        total_price = price * quantity
        self.car_market[brand]['Stock'] -= quantity

        print("\nPurchase successful!")
        print(f"Car: {brand}")
        print(f"Quantity: {quantity}")
        print(f"Price per car: ${price}")
        print(f"Total price: ${total_price}")
        print(f"Remaining stock: {self.car_market[brand]['Stock']}") # TODO replace log

        logging.info(f"Successful purchase: {brand}, quantity: {quantity}, total: ${total_price}")





                




       
