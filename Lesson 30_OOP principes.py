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
            pass  

class Duck(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def showInfo(self):
            pass        

if __name__ == "__main__":
    
    cat_obj = Cat(input("Tom"))
                 