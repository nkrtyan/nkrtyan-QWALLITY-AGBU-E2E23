import logging

class CarMarket:

    car_info = {

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


    def check_car_existence(self, brand):
        if brand in self.car_info:
            return True
        else:
            return False

    def show_market(self):
        print("\n AVAILABLE CARS: \n")

        for car, details in self.car_info.items():
            print(f"{car} - Price: {details["Price"]}$ - Stock: {details["Stock"]}")
        logging.info("Car Market shows successfully")    

    def calculate_price(self,brand):
        if self.check_car_existence(brand):
            return self.car_info[brand]["Price"]
        else:
            return None
            
        
class MyCar(CarMarket):
    
    def calculate_price(self,brand):
        original_price = super().calculate_price(brand)

        if original_price is None:
            return None

        if brand == "BMW":
            discounted_price = original_price * 0.8
            return discounted_price
        else:
            return original_price   


    def search_car(self,brand):
        print("\n Searched Car Info: ")
        if self.check_car_existence(brand):

            original_price = super().calculate_price(brand)
            final_price = self.calculate_price(brand)
            stock = self.car_info[brand]["Stock"]

            print(f"Brand: {brand}")
            print(f"Original price: {original_price}$")
            print(f"Final price: {final_price}$")
            print(f"Stock: {stock}")

            logging.info(f"Successful search: {brand}")

        else:
            print(f"{brand} is not available in the market \n")
            logging.error(f"Unsuccessful search: {brand} does not exist")


    def buy_car(self, brand, quantity):
        print("\n Purchased Car Info: ")
        if not self.check_car_existence(brand):
            print(f"{brand} isn't available \n")
            logging.error(f"Purchase failed: {brand} does not exist")
            return

        if type(quantity) != int or quantity <= 0:
            print("Invalid quantity. Please enter a positive number. \n")
            logging.error(f"Purchase failed: Invalid quantity {quantity}")
            return

        stock = self.car_info[brand]["Stock"]

        if quantity > stock:
            print(f"Insufficient stock. Available cars: {stock} \n")
            logging.error(f"Purchase failed: Insufficient stock for {brand}")
            return


        price = self.calculate_price(brand)
        total_price = price * quantity

        self.car_info[brand]["Stock"] -= quantity

        print(f"Successfully purchased {quantity} {brand} car(s).")
        print(f"Total price: {total_price}$")
        print(f"Remaining stock: {self.car_info[brand]['Stock']}")

        logging.info(f"Successful purchase: {quantity} {brand} car(s), total {total_price}$")





                




       
