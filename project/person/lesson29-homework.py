sports={
    "swimming":{
        "price":40000,
        "sessions": 16  
   },
"Tesnnis":{
    "price":50000,
    "session":10
},
}
class sport:
    def __init__(self, name, price, sessions):
        self.name=name
        self.price=price
        self.sessions=sessions

    def calculate_price(self):
            result=self.price/self.sessions
            print(f"{self.name} one session price{result} AMD")


Swimming_obj=sport(
     "Swimming"
     
     )
Tennis_obj=sport("Tennis")
Swimming_obj.calculate_price()
Tennis_obj.calculate_price()


