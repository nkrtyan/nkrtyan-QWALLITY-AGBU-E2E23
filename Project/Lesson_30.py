class Animal:
    def __init__(self,name):
        self.name = name 

    def show_info(self, name):
        print(f"{name}")

    def move():
        pass


class Cat(Animal):
    def __init__(self,name,age,height):
        super().__init__(name)
        self.age = age 
        self.height = height 

    def show_info(self):
        print(f"{self.name}, {self.age} տարեկան,{self.height} կգ")
        

if __name__ =="__main__":
    cat = Cat("Mursik", 3, 12)
    cat.show_info()