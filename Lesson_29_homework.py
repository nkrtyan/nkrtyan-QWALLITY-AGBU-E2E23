# Create a Python program to calculate the price of one training session for different sports.
import math  # TODO, math is not used, remove import

# Keep the sports information in a global dictionary.
data={  # TODO, use clear name: sports; add spaces around "=" in all places
    "Swimming": {"price":40000,  # TODO, add space after ":"
                 "session": 16},
    "Tennis": {"price": 50000,
               "session": 10}
}

# Create a Sport class that has a name, price, and number of sessions.
class Sport():  # TODO, not recomended  "()" and empty line after class: class Sport:

    def __init__(self, name, price, session):  # TODO, use "sessions" name, it is number of sessions
        self.name=name
        self.price=price
        self.session=session

# Create a method that calculates the price of one session.  # TODO, indent comment inside class with 4 spaces
    def price_per_session(self):
        return self.price/self.session, # TODO, print directly here

# Create objects for swimming_obj and tennis_obj.
# TODO, keep 2 empty lines after class, add main block, use for loop with sports.items() instead of creating each object by hand
swimming_obj=Sport("Swimming",data["Swimming"]["price"], data["Swimming"]["session"])
tennis_obj=Sport("Tennis",data["Tennis"] ["price"], data["Tennis"] ["session"])  # TODO, no space between ["Tennis"] ["price"]; add space after ","

Sport.price_per_session(swimming_obj)  # TODO, remove these 2 lines, result is not used
Sport.price_per_session(tennis_obj)

# Print the session price for each sport.
print(f"{swimming_obj.name} - {Sport.price_per_session(swimming_obj)} AMD per session")  # TODO, call method from object: swimming_obj.price_per_session()
print(f"{swimming_obj.name} - {Sport.price_per_session(tennis_obj)} AMD per session")  # TODO, bug: prints "Swimming" for tennis, use tennis_obj.name; remove extra empty lines below

# Nel, working code

    

