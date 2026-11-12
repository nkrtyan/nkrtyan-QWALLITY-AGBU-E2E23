# Create a Python program to calculate the price of one training session for different sports.
import math

# Keep the sports information in a global dictionary.
data={
    "Swimming": {"price":40000,
                 "session": 16},
    "Tennis": {"price": 50000,
               "session": 10}
}

# Create a Sport class that has a name, price, and number of sessions.
class Sport():

    def __init__(self, name, price, session):
        self.name=name
        self.price=price
        self.session=session

# Create a method that calculates the price of one session.
    def price_per_session(self):
        return self.price/self.session

# Create objects for swimming_obj and tennis_obj.
swimming_obj=Sport("Swimming",data["Swimming"]["price"], data["Swimming"]["session"])
tennis_obj=Sport("Tennis",data["Tennis"] ["price"], data["Tennis"] ["session"])

Sport.price_per_session(swimming_obj)
Sport.price_per_session(tennis_obj)

# Print the session price for each sport.
print(f"{swimming_obj.name} - {Sport.price_per_session(swimming_obj)} AMD per session")
print(f"{swimming_obj.name} - {Sport.price_per_session(tennis_obj)} AMD per session")

    

