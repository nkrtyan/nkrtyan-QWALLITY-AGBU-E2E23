sports = {
    "swimming" :{  # TODO, no space before ":", add space after it: "swimming": {
        "price": 40000, "session": 16
        },
    "tennis" :{
        "price": 50000, "session": 10
        },
}

class Sport:
    def __init__(self, name, price, session):  # TODO, use "sessions" name, it is number of sessions
        self.name = name
        self.price = price
        self.session = session

    def one_session_price(self):
        print(f"{self.name} - {self.price / self.session} AMD per session")

# TODO, keep 2 empty lines after class, add main block
# TODO, use for loop with sports.items() instead of creating each object by hand
swimming_obj = Sport("Swimming", sports["swimming"]["price"], sports["swimming"]["session"])
tennis_obj = Sport("Tennis", sports["tennis"]["price"], sports["tennis"]["session"])
swimming_obj.one_session_price()
tennis_obj.one_session_price()

# Nel, working code, good:)