class Animal:
    def __init__(self, name):
        self.name = name
        
    def showinfo(self):
        self.info = 25
        print(f'Show method that should be changed, {self.info}')
    
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
        
    def showinfo(self):
        self.info = 30
        print(f'Already changed showinfo, {self.info}')
        
class Mouse(Animal):
    def smth(self):
        print(f'smth')       
    
    
class Duck(Animal):
    pass


x = Animal("Cat")
x.print_name()
x.showinfo()
cat_animal = Cat("Kiti", 3, 0.3)
cat_animal.showinfo()
cat_animal.print_name()
Mousee_animal = Mouse("Miki")
Mousee_animal.print_name()
duck_animal = Duck("Badik")
duck_animal.print_name()
            