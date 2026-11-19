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

    def __init__(self, brand):
        self.brand = brand

    def check_car_existence(self, brand):
        if brand in self.car_market:
            logging.info(f"This is the model of this car. - {brand}")
            return True
        else:
            logging.error(f"The car with this {brand} brand name does not exist")
            return False
        #FIX logs
    
    
    def show_market(self):
        print("\n========== CAR MARKET ==========")

        for brand, details in self.car_market.items():
            logging.info(
                f"Brand: {brand} | "
                f"Price: {details['Price']} | "
                f"Stock: {details['Stock']}"
            )
            #FIX (brand,price,stock in logs)
    
    
    def calculate_price(self, brand):
        if self.check_car_existence(brand):
            price = self.car_market[brand]['Price']
            logging.info(f"Here the car {brand} model and the price is ${price}.")
            return self.car_market[brand]['Price']
        else:
            logging.info(f"Car {brand} is unavailable for price calculation.")
            return None
        

class MyCar(CarMarket):

    def __init__(self, brand, quantity):
        super().__init__(brand)
        self.quantity = quantity 


    def calculate_price(self, brand):
        original_price = super().calculate_price(brand)
        discount = original_price * 0.8
        
        if original_price is None:
            return None
        elif brand == "BMW":
            logging.info(f"New price {discount}($) after 20% discount for this {brand} car")
            return discount #FIX discount, logs
        else:
            logging.info(f"The price is {original_price} for {brand} car.")
            return original_price
        
        
    def search_car(self, brand):
        if self.check_car_existence(brand):
            logging.info(f"Successful search: {brand} is available.")
            original_price = super().calculate_price(brand)
            final_price = self.calculate_price(brand)
            stock = self.car_market[brand]['Stock']

            logging.info(f"\nCar found: {brand}")
            logging.info(f"Original price: ${original_price}")
            logging.info(f"Final price: ${final_price}")
            logging.info(f"Available stock: {stock}")
        else:
            logging.info(f"Unsuccessful search: {brand} is unavailable.")

            # if brand == "BMW":
            #     print("Discount applied: 20%") # FIX replace in calculate function

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

        logging.info("\nPurchase successful!")
        logging.info(f"Car: {brand}")
        logging.info(f"Quantity: {quantity}")
        logging.info(f"Price per car: ${price}")
        logging.info(f"Total price: ${total_price}")
        logging.info(f"Remaining stock: {self.car_market[brand]['Stock']}") # FIX replace log





                




       
