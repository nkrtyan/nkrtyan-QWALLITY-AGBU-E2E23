sports = {
    "Swimming": {"price": 40000, "sessions": 16},
    "Tennis": {"price": 50000, "sessions": 10}
}

class Sport:
    def __init__(self, name, price, n_sessions):
        self.name = name
        self.price = price
        self.sessions = n_sessions

    def calculate_session_price(self):
        return self.price / self.sessions
    

swimming_obj = Sport(
    "Swimming",
    sports["Swimming"]["price"],
    sports["Swimming"]["sessions"]
)

tennis_obj = Sport(
    "Tennis",
    sports["Tennis"]["price"],
    sports["Tennis"]["sessions"]
)


print(f"{swimming_obj.name} - {swimming_obj.calculate_session_price()} AMD per session")
print(f"{tennis_obj.name} - {tennis_obj.calculate_session_price()} AMD per session")