import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S', 
    filename='class_work.log',
    filemode='a+', 
    encoding='utf-8' 
)

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname

#     def print_name(self):
#         print(f"{self.name} {self.surname}")


# class Student(Person):
#     def __init__(self, name, surname, year, course_type):
#         Person.__init__(self, name, surname)
#         self.year = year
#         self.course_type = course_type

#     def print_name(self):
#         print(f"The student with this {self.name} first name and {self.surname} last name, is studying in {self.course_type} educational center, in {self.year} this year. ")
#         logging.info(f"The student with this {self.name} first name and {self.surname} last name, is studying in {self.course_type} educational center, in {self.year} this year. ")

# if __name__ == "__main__":
#     input_name = input("Enter your first name: ")
#     input_surname = input("Enter your last name: ")
#     course_type = input("Enter the name of the educational center in which you are studying: ")
#     input_year = input("Enter the year you are currently studying in: ")
#     student_input = Student(input_name, input_surname, input_year, course_type)
#     student_input.print_name()

class Animal:
    def __init__(self, name):
        self.name = name

    def showInfo(self):
        print(f"The name is: {self.name}")

    def move(self):
        pass


class Cat(Animal):
    def __init__(self, name, age, height):
        super().__init__(name)
        self.age = age
        self.height = height

    def showInfo(self):
        print(f"Show all the information about the Cat. Name - {self.name}, Age - {self.age}, Height - {self.height}")
        logging.info(f"Show all the information about the Cat. Name - {self.name}, Age - {self.age}, Height - {self.height}")

# class Mouse(Animal):
#     def __init__(self, name, age, height):
#             super().__init__(name)
#             self.age = age
#             self.height = height

#     def showInfo(self):
#         print(f"Show all the information about the Mouse. Name - {self.name}, Age - {self.age}, Height - {self.height}")
#         logging.info(f"Show all the information about the Mouse. Name - {self.name}, Age - {self.age}, Height - {self.height}")

# class Duck(Animal):
#     def __init__(self, name, age, height):
#             super().__init__(name)
#             self.age = age
#             self.height = height
    
#     def showInfo(self):
#         print(f"Show all the information about the Mouse. Name - {self.name}, Age - {self.age}, Height - {self.height}")
#         logging.info(f"Show all the information about the Mouse. Name - {self.name}, Age - {self.age}, Height - {self.height}")

         
if __name__ == "__main__":
    animal_name = input("Enter the name of animal: ")
    animal_age = input("Enter the age of animal: ")
    animal_height = input("Enter the height of animal: ")
    animal_obj = Cat(animal_name, animal_age, animal_height)
    # animal_obj = Mouse(animal_name, animal_age, animal_height)
    # animal_obj = Duck(animal_name, animal_age, animal_height)
    animal_obj.showInfo()
