from logger_config import logger

class CarMarket:
    car_market_data = {
    "BMW": {
        "price": 50000,
        "quantity": 5
    },
    "Toyota": {
        "price": 30000,
        "quantity": 5
    },
    "Ford": {
        "price": 35000,
        "quantity": 5
    },
    "Honda": {
        "price": 32000,
        "quantity": 5
    },
    "Kia": {
        "price": 34000,
        "quantity": 5
    },
    "BYD Sealion": {
        "price": 40000,
        "quantity": 5
    },
    "Bugatti": {
        "price": 2500000,
        "quantity": 5
    },
    "Audi": {
        "price": 55000,
        "quantity": 5
    },
    "Mercedes-Benz": {
        "price": 60000,
        "quantity": 5
    },
    "Hyundai": {
        "price": 27000,
        "quantity": 5
    }
}
    def __init__(self, brand):
        self.self = brand
        pass
    def check_car_existence(self, brand):
        if brand in self.car_market_data:
            logger.info(f'{brand} found successfully.')
            return brand
        else:
            logger.error(f'Brand {brand} is not available in our market.')
            return False

    def show_market(self):
        for brand, info in self.car_market_data.items():
            logger.info(f'Brand: {brand}, Price: ${info['price']}, Stock: {info['quantity']}')
      

    def calculate_price(self, brand):
        if self.check_car_existence(brand):
            logger.info(
            f'The cost calculation was successful: '
            f'{brand} - ${self.car_market_data[brand]["price"]}'
        )
            return self.car_market_data[brand]["price"]

        else:
            logger.error(f'calculate_price Brand {brand} is not available.')
    
class MyCar(CarMarket):
    def calculate_price2(self, brand, discount):
        price = self.calculate_price(brand)

        if price and brand == 'BMW':
            discounted_price = price * discount
            logger.info(f"{discounted_price} — price with a 20% discount")
            return discounted_price

        elif price:
            logger.info(f"{brand}- ${price}")
            return price

        else:
            logger.warning(f"{brand} is not available.")
            return None
        
    def search_car(self, brand):
        check_car = self.check_car_existence(brand)
        if check_car and brand == 'BMW':
            logger.info(
            f"Original price: ${self.car_market_data[brand]['price']}\n"
            f"Price with 20% discount: ${self.car_market_data[brand]['price'] * 0.8}\n"
            f"Available cars in stock: {self.car_market_data[brand]['quantity']}"
        )
        elif check_car:
            logger.info(
            f"Original price: ${self.car_market_data[brand]['price']}\n"
            f"Discounts are available for BMW only.\n"
            f"Available cars in stock: {self.car_market_data[brand]['quantity']}"
        )
        else:
            logger.error(f"{brand} is not available in our market.")
        
    def buy_car(self, brand, quantity):
        if brand not in self.car_market_data:
            logger.error('This brand is not available in our market.')
        if brand in self.car_market_data and quantity <= self.car_market_data[brand]['quantity']:
            all_sum = quantity*self.car_market_data[brand]['price']
            self.car_market_data[brand]['quantity'] -= quantity
            logger.info( f'The total price for {quantity} car(s) is: ${all_sum}')
        if quantity > self.car_market_data[brand]['quantity']:
            logger.info(f'Only {self.car_market_data[brand]["quantity"]} car(s) of this brand are available in stock.')
        
      
        

            

        

    
