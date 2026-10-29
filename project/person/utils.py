import data

def get_full_name(name, surname):
    full_name=f"{data.person_info[name]},{data.person_info [surname]}"
    return full_name

def print_person(full_name):
    print("Person's information: ",full_name)