from .data import my_data

def get_full_name(name, surname):
    return f"{name} {surname}"


def print_person():
    print(f"Full name: {get_full_name(my_data['name'], my_data['surname'])}")