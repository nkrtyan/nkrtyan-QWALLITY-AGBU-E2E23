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
} # TODO, keep this format

class Sport:  # TODO, keep 2 empty lines before class
    def __init__(self, name, price, n_sessions):  # TODO, recomended to use same name for argument and attribute: sessions
        self.name = name
        self.price = price
        self.sessions = n_sessions

    def calculate_session_price(self):
        return self.price / self.sessions # TODO, print directly here
    

# TODO, add main block
# TODO, use for loop with sports.items() instead of creating each object by hand
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
# Nel, working code, have a look to TODO