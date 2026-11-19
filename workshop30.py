class Animal:
    def __init__(self, name):
        self.name = name
        
    def show_info(self):
        print(f"Animal name is {self.name}")
        
    def move(self):
        print(f"{self.name} is moving")
        
        
class Cat(Animal):
    def __init__(self, name, age, height):
        Animal.__init__(self, name)
        self.age = age
        self.height = height
    
    def show_info(self):
        print(f"{self.name} is {self.age} year old and has {self.height} height.")
    
    
class Mouse(Animal):
    def __init__(self, name, sound):
        Animal.__init__(self, name)
        self.sound = sound
    
    def talk(self):
        print(f"{self.name}'s sound is {self.sound}")


class Duck(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color
    
    def show_info(self):
        print(f"{self.name}'s color is {self.color}.")


if __name__ == "__main__":
    cat_name = input("Enter cat's name: ")
    age = input("Enter cat's age: ")
    height = input("Enter cat's height: ")

    mouse_name = input("Enter mouse's name: ")
    sound = input("Enter mouse's sound: ")

    duck_name = input("Enter duck's name: ")
    color = input("Enter duck's color: ")

    cat = Cat(cat_name, age, height)
    mouse = Mouse(mouse_name, sound)
    duck = Duck(duck_name, color)

    cat.show_info()
    cat.move()

    mouse.talk()
    mouse.move()

    duck.show_info()
    duck.move()
    