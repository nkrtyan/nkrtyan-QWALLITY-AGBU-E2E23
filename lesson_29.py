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

class SPORT:  # TODO, class name should be CamelCase: Sport, remove empty lines below


    def __init__(self, name, price, numberofsessions):  # TODO, use snake_case: number_of_sessions
        self.name = name
        self.price = price
        self.numberofsessions = numberofsessions

    # TODO, keep two lines between methods/functions
    def get_session_price(self):
        return f'{self.name} = {self.price/self.numberofsessions} AMD per session' 
    
    
# TODO, remove commented code below
# sport1 = Sport(list(sports.keys())[0],sports['Swimming']['price'], sports['Swimming']['sessions'])
# sport2 = Sport(list(sports.keys())[1], sports['Tennis']['price'], sports['Tennis']['sessions'])

# TODO, need main block, 
for sport_name, sport_info in sports_data.items():
    sport = SPORT ( # TODO, no need space fbetween SPORT (
        sport_name ,  # TODO, no need space before ","
        sport_info['price'], 
        sport_info['sessions']
        )
    print(sport.get_session_price()) # TODO, move print i the function

# Nel, the code is correct
