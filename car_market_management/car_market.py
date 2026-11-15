import logging
import os
import shutil
import pandas as pd


class CarMarket:
    def __init__(self):
        self.cars = {
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
        
    def check_car_existence(self, brand):
        return brand in self.cars

    def show_market(self):
        for brand, info in self.cars.items():
            print(f"Brand: {brand}, Price: ${info['price']}, Stock: {info['stock']}")
    def check_car_existence(self, brand):
            return brand in self.cars
            
    def show_market(self):
        for brand, price in self.check_car_existence:
            print(f"Brand: {brand}, Price: ${price}")
            
    def calculate_price(self, brand):
        if self.check_car_existence(brand):
            return self.cars[brand]["price"]
            return None
                
class MyCar(CarMarket):
    def calculate_price(self, brand):
        price = super().calculate_price(brand)
        if price is not None:
            return None
        if brand == "BMW":
            return price * 0.8
        return price  
    
    def search_car(self, brand):
        if self.check_car_existence(brand):
            orig_price = super().calculate_price(brand)
            final_price = self.calculate_price(brand)
            stock = self.cars[brand]["stock"]
            print(f"Car found: {brand} - Original Price: ${orig_price}, Final Price: ${final_price}, Stock: {stock}")
        else: 
            print(f"Car not found: {brand}")
    
    def buy_car(self, brand, quantity):
        if not self.check_car_existence(brand):
            print("Car not found")
            return
    stock = self.cars[brand]["stock"]
    if quantity > stock:
        print(f"Not enough stock for {brand}. Available stock: {stock}")
        return
    self.cars[brand]["stock"] -= quantity
    total_price = self.calculate_price(brand) * quantity
    print(f"Successfully purchased {quantity} {brand}(s) for ${total_price}. Remaining stock: {self.cars[brand]['stock']}")
    
    