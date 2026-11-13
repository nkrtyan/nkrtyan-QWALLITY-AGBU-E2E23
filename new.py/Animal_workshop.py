class Animal:
    def __init__(self, name):
        self.name = name
        
    def showinfo(self):
        print("Show method that should be changed")
    
    def move(self):
        print(f"{self.name} ")
        
    def print_name(self):
        print(self.name)
          

class Cat(Animal):
    def __init__ (self,name,  age, height):
        Animal.__init__(self, name)
        self.age = age
        self.height = height
        
    def print_name(self):
        print(f"name of cat is {self.name}, age is {self.age}, height is {self.height}")
        
class Mouse(Animal):
    pass         
    
    
class Duck(Animal):
    pass


cat_animal = Cat("Kiti", 3, 0.3)
Mousee_animal = Mouse("Miki")
cat_animal.print_name()
Mousee_animal.print_name()
duck_animal = Duck("Badik")
duck_animal.print_name()
            