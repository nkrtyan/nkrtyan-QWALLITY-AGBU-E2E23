person = {"name": "Zara", "surname": "Kayseryan"}

from .data import person


def get_full_name(name, surname):
    return f"{name} {surname}"


def print_person():

    print(get_full_name(person["name"], person["surname"]))
    

