sports = {                                          # FIXED, file has no .py extension, add it; remove empty lines inside dictionary
    'swimming': {'price': 40000, 'sessions': 16},   # FIXED, 16 is number of sessions, not duration, rename key to 'sessions'
    'tennis': {'price': 50000, 'sessions': 10}
}


class SportSessions:  # FIXED, recomended CamelCase without "_" and "()": class SportSession:

    def __init__(self, name, price, number_of_session):
        self.name = name
        self.price = price
        self.number_of_session = number_of_session

    def calculate_session_price(self):  # FIXED, it calculates price, rename to calculate_session_price
        session_price = self.price / self.number_of_session
        print(f"{self.name} - {session_price} AMD per session")


# FIXED, keep 2 empty lines after class, add main block
# FIXED, use for loop with sports.items() instead of creating each object by hand
if __name__ == "__main__":
 
 for sport_name, sport_data in sports.items():

    sport_obj = SportSessions(
        sport_name,
        sport_data['price'],
        sport_data['sessions']
    )    

    sport_obj.calculate_session_price()

    


# Nel, working code
