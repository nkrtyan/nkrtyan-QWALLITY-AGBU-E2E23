import logging

class CarMarket:
    car_market_data = {
        "BMW": {
            "Price": 50000,
            "Stock": 5,
        },
        "Toyota": {
            "Price": 30000,
            "Stock": 5,
        },
        "Ford": {
            "Price": 35000,
            "Stock": 5,
        },
        "Honda": {
            "Price": 32000,
            "Stock": 5,
        },
        "Kia": {
            "Price": 34000,
            "Stock": 5,
        },
        "BYD Sealion": {
            "Price": 40000,
            "Stock": 5,
        },
        "Bugatti": {
            "Price": 2500000,
            "Stock": 5,
        },
        "Audi": {
            "Price": 55000,
            "Stock": 5,
        },
        "Mercedes-Benz": {
            "Price": 60000,
            "Stock": 5,
        },
        "Hyundai": {
            "Price": 27000,
            "Stock": 5,
        },
    }

    def __init__(self, brand):
        self.brand = brand

    # Validates if the car brand exists in the market
    def check_car_existence(self, brand):
        if brand not in self.car_market_data:
            logging.error(f"The car with this {brand} brand name does not exist")
            return False
        else:
            logging.info(f"This is the model of this car. - {brand}")
            return True

    # Display all available cars, prices, and stock
    def show_market(self):
        logging.info("Show all cars in the market.")
        for model, details in self.car_market_data.items():
            logging.info(
                        f"Car model - {model}, "
                        f"Car price - {details['Price']}, " 
                        f"Car stock quantity - {details['Stock']} "
                    )
            
    # Base Pricing Method․ Returns the original price of a car
    def calculate_price(self, brand):
        if self.check_car_existence(brand):
            price = self.car_market_data[brand]['Price']
            logging.info( f"The car with this {brand} model and with this current price {price} ($).")
            return price
        else:
            logging.error(f"The car with this {brand} model does not exist.")
            return None


class MyCar(CarMarket):
    def __init__(self, brand, quantity):
        super().__init__(brand)
        self.quantity = quantity

    # Method Overriding (Polymorphism). Applies a 20% discount for BMW
    def calculate_price(self, brand):
        original_price = super().calculate_price(brand)
        discount = (original_price * 0.2)
        if original_price is None:
            return None
        elif brand == "BMW":
            final_price = original_price - discount
            logging.info(f"New price {final_price} ($) after 20% discount for this {brand} car")
            return final_price
        else:
            return original_price#TODO LOGING, if not

    # Search Method. Displays full car details using inherited methods
    def search_car(self, brand):
        if self.check_car_existence(brand):
            original_price = self.car_market_data[brand]['Price']
            final_price = self.calculate_price(brand)
            av_stock = self.car_market_data[brand]['Stock']
            logging.info(f"Search the car"
                f"\nCar model - {brand}, "
                f"\nOriginal price before discount - {original_price} ($), "
                f"\nFinal price after discount - {final_price} ($), "
                f"\nAvailable stock - {av_stock}, "
            )

    # Purchase Method. Validates quantity/stock and updates it
    def buy_car(self, brand, quantity):
        if self.check_car_existence(brand):
            if quantity <= 0:
                logging.error("How many car(s) do you want to buy? Invalid quantity.")
            elif quantity > self.car_market_data[brand]['Stock']:
                logging.error(f"There is not enough {brand} cars in the stock.")
            else:
                total_price = self.calculate_price(brand) * quantity
                self.car_market_data[brand]['Stock'] -= quantity 
                total_cars = self.car_market_data[brand]['Stock']
                # logging.info(f"Total price of this {brand} = {total_price} ($)")
                # logging.info(f"There is/are {total_cars} car(s) after buying cars.")
                logging.info(f"Congratulations!! You bought {quantity} {brand} car(s) "
                f"successfuly, it's cost {total_price} ($). "
                f"And there is/are {total_cars} car(s) in the stock.")
        else:
            logging.error(f"This {brand} car doesn't exist.")