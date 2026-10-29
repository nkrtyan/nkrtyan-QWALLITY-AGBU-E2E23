from .data import person_info

def get_full_name(name, surname): # TODO, no need extra line
    return f"{name} {surname}"

def print_person():
    person_info["name"] = input("Enter your name: ") # TODO, keep name and surmname directly in josn, no need input in this case
    person_info["surname"] = input("Enter your surname: ")

    name = person_info["name"] # TODO, would be better to get info in main block, and pass to function 
    surname = person_info["surname"]
    
    full_name = get_full_name(name, surname) 
    print(f"Full Name: {full_name}")