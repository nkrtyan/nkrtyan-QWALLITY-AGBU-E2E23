import math  # TODO, math is not used, remove import


sport_1 = {  # TODO, use one dictionary for all sports, like {"Swimming": {"price": 40000, "sessions": 16}, ...}
    "sport_type": "swimming",
    "month_price": 40000,
    "session":16  # TODO, add space after ":" in all places
}


sport_2 = {
    "sport_type": "tennis",
    "month_price":50000,
    "session":10
}


class Sport:
    def __init__(self, sport_type, price, session):  # TODO, use "sessions" name, it is number of sessions
            self.sport_type = sport_type  # TODO, use 4 spaces for indentation in all lines
            self.price = price
            self.session = session

            
    def priceOf_one_session(self):  # TODO, keep only 1 empty line between methods, recomended to se snake_case: calculate_session_price
         return self.price / self.session
    

# TODO, add main block
# TODO, use for loop with sports.items() instead of creating each object by hand
swimming_obj = Sport(sport_1["sport_type"],sport_1["month_price"],sport_1["session"])
print(swimming_obj.priceOf_one_session())  # TODO, print full text: Swimming - 2500.0 AMD per session; add space after "," in all places
tennis_obj = Sport(sport_2["sport_type"],sport_2["month_price"],sport_2["session"])
print(tennis_obj.priceOf_one_session())

# Nel, working code, add also logging