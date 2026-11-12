sport_data = {
    "Swimming": {"Price": 40000, "Sessions": 16},
    "Tennis": {"Price": 50000, "Sessions": 10}
}

class Sport:
    def __init__(self, name, price, sessions):
        self.name=name
        self.price=price
        self.sessions=sessions


    def show(self):
        print("Sport Name:", self.name)
        print("Sport Price:", self.price)
        print("Sport Sessions:", self.sessions)

    def calculate_total_cost(self):
        return self.price / self.sessions    
swimming_obj = Sport("Swimming", sport_data["Swimming"]["Price"], sport_data["Swimming"]["Sessions"])
tennis_obj = Sport("Tennis", sport_data["Tennis"]["Price"], sport_data["Tennis"]["Sessions"])
        
        
print(f"Swimming: {swimming_obj.calculate_total_cost()} AMD per session")
print(f"Tennis: {tennis_obj.calculate_total_cost()} AMD per session")