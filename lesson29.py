sports = {
    "Swimming": 
    {
        "price": 40000, 
        "sessions": 16},
    "Tennis": 
    {
        "price": 50000, 
        "sessions": 10
        }
} 


class Sport:  
    def __init__(self, name, price, sessions):  
        self.name = name
        self.price = price
        self.sessions = sessions

    def calculate_session_price(self):
        print(self.price / self.sessions)  
    

if __name__ == "__main__":
    for name, sport_info in sports.items():
        sport_obj = Sport(
            name,
            sport_info["price"],
            sport_info["sessions"]
        )
        print(f"{sport_obj.name} session price is: ")
        sport_obj.calculate_session_price()
        
# Nel, working code, have a look to TODO