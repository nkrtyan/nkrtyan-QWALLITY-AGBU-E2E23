sports_data = {
    'Swimming': {
        'price': 40000,
        'sessions': 16
    },
    'Tennis': {
        'price': 50000,
        'sessions': 10
    }
}

class Sport:  # TODO, class name should be CamelCase: Sport, remove empty lines below
    def __init__(self, name, price, number_of_sessions):  # TODO, use snake_case: number_of_sessions
        self.name = name
        self.price = price
        self.number_of_sessions = number_of_sessions

    # TODO, keep two lines between methods/functions
    def get_session_price(self):
        return f'{self.name} = {self.price/self.number_of_sessions} AMD per session' 

# TODO, need main block, 
def get_sports():
    for sport_name, sport_info in sports_data.items():
        sport = Sport( # TODO, no need space fbetween SPORT (
            sport_name,  # TODO, no need space before ","
            sport_info['price'],
            sport_info['sessions']
        )
        print(sport.get_session_price()) # TODO, move print i the function
    

if __name__ == '__main__':
    get_sports()


# Nel, the code is correct
