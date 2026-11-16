from logger_config import setup_logging
import logging

class CarMarket:
    car_market_data = {
        "BMW": {"price": 50000, "stock": 5},
        "Toyota": {"price": 30000, "stock": 5},
        "Ford": {"price": 35000, "stock": 5},
        "Honda": {"price": 32000, "stock": 5},
        "Kia": {"price": 34000, "stock": 5},
        "BYD": {"price": 40000, "stock": 5},
        "Bugatti":{"price": 2500000, "stock": 5},
        "Audi": {"price": 55000, "stock": 5},
        "Mercedes-Benz": {"price": 60000, "stock": 5},
        "Hyundai": {"price": 27000, "stock": 5}
        } 
    
    def __init__(self, brand):
        self.brand = brand
        
        
    def check_car_existence(self, brand):
        if brand not in self.car_market_data:
            logging.info (f"{brand} doesn't exist: ")
            return False
        else:
            logging.info (f"{brand} exists: ")
            return True
        
    def show_market(self):
        print(f"all available  car brands, prices, and stock quantities are desplayed: ")
        
        for key, value in self.car_market_data.items():
            print(f"{key} price: {value['price']}, stock: {value['stock']}")  # OR print(f'{key}  {value}')            
                
    def calculate_price(self, brand):
        if brand in self.car_market_data:
            return self.car_market_data[brand] ["price"]
        else:
            return None
            
            
class MyCar(CarMarket):
    
    def __init__(self, brand, quantity):
        super().__init__(brand)
        self.quantity = quantity

    def calculate_price(self, brand):
            for key, value in self.car_market_data.items():
                if key == brand:
                    if brand == "BMW":
                        logging.info(f"{brand} has disacount 20 percent,price will be: ")
                        return value["price"] * 0.8
                    else:
                        return value["price"]
                    
            logging.info(f"{brand} dosn't exist for calculate")
            return None

    def search_car(self, brand):  #Search for a car and display its brand, original price, final price, and available stock. Display a message if the car does not exist.
        for key, value in self.car_market_data.items():
            if key == brand:
                final_price = self.calculate_price(brand)
                logging.info(f"{brand} searched successfully")
                print(f"{key} original price: {value['price']}, final price: {final_price} stock: {value['stock']}")  # OR print(f'{key}  {value}')
                return
        
        logging.info(f"{brand} doesn't exist in our market")    
        print(f"{brand} doesnt exist in our market")                                            

    def buy_car(self, brand, quantity):     #Check availability and stock, calculate the total price, and reduce stock,after a successful purchase.#  Reject invalid quantities or insufficient stock without changing the stock.
        for key, value in self.car_market_data.items():
             if key == brand:
                 if quantity <= 0:
                     logging.error(f"Invalid quantity: {quantity}. ")
                     print("Invalid quantity")
                     return
                 if quantity <= value["stock"]:
                      total_price = self.calculate_price(brand) * quantity
                      value["stock"] -= quantity
                      logging.info(f"Purchase successful: {brand},quantity: {quantity}, total price: {total_price} ")
                      print(f"{brand} is available and total_price is {total_price}. available stok is: {value['stock']}: ")
                      return
                 else:
                     logging.info((f"{brand} isnt available, stock is empty"))
                     print(f"{brand} isnt available, stock is empty")
                     return
                     
                     
        logging.info((f"brand does not exist for buying"))
        print(f"brand does not exist for buying")                          
    


    
        
    



    
     
    #  car_name = CarMarket("BMW")
    #  print(car_name.check_car_existence("BMW"))
    #  car_name.show_market()
    #  print("The original price of that brand", car_name.calculate_price("BMW"))    
    #  child_car = MyCar("BMW",2)
    #  print(child_car.calculate_price("BMW"))
    #  child_car.search_car("BMW")
    #  child_car.buy_car("BMW", 2)
    # #  child_car.buy_car("kiwi",5)


 