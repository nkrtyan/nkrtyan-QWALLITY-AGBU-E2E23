# TODO, file should not start with empty line, remove this line
import logging

sports_info = {
    "Swimming": {
        "payment": 40000,
        "sessions": 16
    },
    "Tennis": {
        "payment": 50000,
        "sessions": 10
    },
}

logging.basicConfig( # Nel, good when using what learnt :)
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S', 
    filename='sport_info.log',
    filemode='a+', 
    encoding='utf-8' 
)

class Sport:  # TODO, keep 2 empty lines before class
    def __init__(self, name, price, session):  # TODO, use "sessions" name, it is number of sessions
        self.name = name
        self.price = price
        self.session = session


    def calculate_session(self):  # TODO, keep only 1 empty line between methods, rename to calculate_session_price
        one_session = self.price/self.session
        print(f"{self.name} - {one_session} AMD per session")
        logging.info(f"{self.name} - {one_session} AMD per session")


if __name__ == "__main__":
   for sport_name, details in sports_info.items():  
        sport_obj = Sport(sport_name, details["payment"], details["sessions"])
        sport_obj.calculate_session()
# Nel, working code