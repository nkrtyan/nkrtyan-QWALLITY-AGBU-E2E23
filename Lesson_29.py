sport_data = {
    "Swimming": 
    {
        "Price": 40000, 
        "Sessions": 16
     },
    "Tennis": 
    {
        "Price": 50000, 
        "Sessions": 10}
} # TODO< keep this format

class Sport:
    def __init__(self, name, price, sessions):
        self.name = name # TODO, add space before and after =
        self.price=price
        self.sessions=sessions

    # TODO, keep one line between methods
    def show(self):
        print("Sport Name:", self.name)
        print("Sport Price:", self.price)
        print("Sport Sessions:", self.sessions)

    def calculate_total_cost(self):
        return self.price / self.sessions  # TODO, you can directly print here 
     # TODO, no  need to hardcde swimming, instead in data keep sport1 with vaue name: swimming
swimming_obj = Sport("Swimming", sport_data["Swimming"]["Price"], sport_data["Swimming"]["Sessions"])
tennis_obj = Sport("Tennis", sport_data["Tennis"]["Price"], sport_data["Tennis"]["Sessions"])
        
        
print(f"Swimming: {swimming_obj.calculate_total_cost()} AMD per session")
print(f"Tennis: {tennis_obj.calculate_total_cost()} AMD per session")
# Nel, working code