sports = {
    "swimming" :{
        "price": 40000, "session": 16
        },
    "tennis" :{
        "price": 50000, "session": 10
        },
}

class Sport:
    def __init__(self, name, price, session):
        self.name = name
        self.price = price
        self.session = session

    def one_session_price(self):
        print(f"{self.name} - {self.price / self.session} AMD per session")

swimming_obj = Sport("Swimming", sports["swimming"]["price"], sports["swimming"]["session"])
tennis_obj = Sport("Tennis", sports["tennis"]["price"], sports["tennis"]["session"])
swimming_obj.one_session_price()
tennis_obj.one_session_price()