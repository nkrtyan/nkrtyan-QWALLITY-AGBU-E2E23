import math 


sport_1 = {
    "sport_type": "swimming",
    "month_price": 40000,
    "session":16
}


sport_2 = {
    "sport_type": "tennis",
    "month_price":50000,
    "session":10
}


class Sport:
    def __init__(self, sport_type, price, session):
            self.sport_type = sport_type
            self.price = price
            self.session = session

            
    def priceOf_one_session(self):
         return self.price / self.session
    

swimming_obj = Sport(sport_1["sport_type"],sport_1["month_price"],sport_1["session"])
print(swimming_obj.priceOf_one_session())
tennis_obj = Sport(sport_2["sport_type"],sport_2["month_price"],sport_2["session"])
print(tennis_obj.priceOf_one_session())

     
    
