class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def print_name(self):
        print(f"{self.name} {self.surname} ")
        
        
class Student(Person):
    def __init__(self, name, surname, year, course_type = "Qwallity" ):
        Person.__init__(self, name, surname)
        self.year = year
        self.course_type = course_type
        
        
    def print_name(self):
        print(f'{self.name} {self.surname} is learning in {self.course_type} in {self.year}: ')
        
        
        
if __name__ == "__main__":
    input_name = input('Input your name: ')
    input_surname = input('Input your surname: ')
    input_year = input('Input your year: ')
    course_type = input('Input your course_type: ')
    
    #person_input = Person(input_name, input_surname)
    #person_input.print_name()
    
    student_input = Student(input_name, input_surname, input_year, course_type)
    student_input.print_name() 
    
    
    