class Animal:
    def __init__(self, name):
        self.name = name

    def showInfo(self):
        print(f"This is {self.name}")

    def move(self):
        print("I can walk")

class Cat(Animal):
    def __init__(self, name, age, height):
        Animal.__init__(self, name)
        self.age = age
        self.height = height    

    def showInfo(self):
            print(f"{self.name} is {self.age} and has {self.height} ")  

class Mouse(Animal):
    def __init__(self, name, food):
        Animal.__init__(self, name)
        self.food = food

    def showInfo(self):
        print(f"{self.name} like to eat {self.food} ")  

class Duck(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def showInfo(self):
            print(f"{self.name} have {self.color} color")         

if __name__ == "__main__":
    
    cat_obj = Cat(input("Input name for cat: "), age = 4, height = "30 cm")
    cat_obj.showInfo()

    mouse_obj = Mouse(input("Input name for mouse: "), input("Input food that mouse like: "))
    mouse_obj.showInfo()

    duck_obj = Duck(input("Input name for duck: "), input("Input color for duck: "))
    duck_obj.showInfo()

    
            