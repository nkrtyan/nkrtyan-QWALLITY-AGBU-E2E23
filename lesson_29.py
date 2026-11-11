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

class SPORT:
    def __init__(self, name, price, numberofsessions):
        self.name = name
        self.price = price
        self.numberofsessions = numberofsessions
    def get_session_price(self):
        return f'{self.name} = {self.price/self.numberofsessions} AMD per session' 
    
    
# sport1 = Sport(list(sports.keys())[0],sports['Swimming']['price'], sports['Swimming']['sessions'])
# sport2 = Sport(list(sports.keys())[1], sports['Tennis']['price'], sports['Tennis']['sessions'])

for sport_name, sport_info in sports_data.items():
    sport = SPORT (
        sport_name ,
        sport_info['price'], 
        sport_info['sessions']
        )
    print(sport.get_session_price())

