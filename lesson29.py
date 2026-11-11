sport_data = {
    "Swimming":{
        "price": 40000,
        "sessions": 16
    },
    "Tennis":{
        "price": 50000,
        "sessions": 10
    }
}

class Sport:
    def __init__(self, name, price, sessions):
        self.name = name
        self.price = price
        self.sessions = sessions


    def price_one_session(self):
         print(f"{self.name} - {self.price / self.sessions} AMD per session")


swimming_obj = Sport("Swimming", sport_data["Swimming"]["price"], sport_data["Swimming"]["sessions"])
tennis_obj = Sport("Tennis", sport_data["Tennis"]["price"], sport_data["Tennis"]["sessions"])
swimming_obj.price_one_session()
tennis_obj.price_one_session()