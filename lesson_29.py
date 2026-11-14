sports = {
    "swimming": {  # DONE, no space before ":", add space after it: "swimming": {
        "price": 40000, "session": 16
        },
    "tennis": {
        "price": 50000, "session": 10
        },
}

class Sport:
    def __init__(self, name, price, sessions):  # DONE, use "sessions" name, it is number of sessions
        self.name = name
        self.price = price
        self.sessions = sessions

    def one_session_price(self):
        print(f"{self.name} - {self.price / self.sessions} AMD per session")


# DONE, keep 2 empty lines after class, add main block
# DONE, use for loop with sports.items() instead of creating each object by hand
for name, data in sports.items():
    sport_obj = Sport(name.capitalize(), data["price"], data["session"])
    sport_obj.one_session_price()

# Nel, working code, good:)