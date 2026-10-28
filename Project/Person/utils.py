from .data import person_info

def get_full_name(name, surname):
   
    return f"{name} {surname}"

def print_person():
    person_info["name"] = input("Enter your name: ")
    person_info["surname"] = input("Enter your surname: ")

    name = person_info["name"]
    surname = person_info["surname"]
    
    full_name = get_full_name(name, surname)
    print(f"Full Name: {full_name}")