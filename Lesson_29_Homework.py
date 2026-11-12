sports = {
    "Swimming": {
        "price": 40000,
        "sessions": 16
    },
    "Tennis": {
        "price": 50000,
        "sessions": 10
    }
}


class Sport:

    def __init__(self, name, price, sessions):
        self.name = name
        self.price = price
        self.sessions = sessions

    def get_session_price(self):
        session_price = self.price / self.sessions
        return session_price # TODO, you can print directly here


def main():
    for name in sports: # TODO, use sports.items()
        sport_obj = Sport(
            name, 
            sports[name]["price"], 
            sports[name]["sessions"]
        )
        session_price = int(sport_obj.get_session_price())

        print(f"{sport_obj.name} - {session_price} AMD per session")


if __name__ == "__main__":
    main()
# Nel, working code, no comment