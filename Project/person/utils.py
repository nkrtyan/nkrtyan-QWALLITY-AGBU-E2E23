from .data import person

name = person["name"]  #  TODO, get this data in main file and  pass to function
surname = person["surname"]

def get_full_name(name, surname):
    return name + " " + surname

def print_person():
    print(get_full_name(name, surname))