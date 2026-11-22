sport_data = {
    "Swimming":{  # TODO, add space after ":" in all places: "Swimming": {
        "price": 40000,
        "sessions": 16
    },
    "Tennis":{
        "price": 50000,
        "sessions": 10
    }
}

class Sport:  # TODO, keep 2 empty lines before class
    def __init__(self, name, price, sessions):
        self.name = name
        self.price = price
        self.sessions = sessions


    def price_one_session(self):  # TODO, keep only 1 empty line between methods, method name recomended to  be a verb: print_session_price
         print(f"{self.name} - {self.price / self.sessions} AMD per session")  # TODO, use 4 spaces for indentation


# TODO, add main block
# TODO, use for loop with sport_data.items() instead of creating each object by hand
swimming_obj = Sport("Swimming", sport_data["Swimming"]["price"], sport_data["Swimming"]["sessions"])
tennis_obj = Sport("Tennis", sport_data["Tennis"]["price"], sport_data["Tennis"]["sessions"])
swimming_obj.price_one_session()
tennis_obj.price_one_session()
# Nel, working code, add also logging