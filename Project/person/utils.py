from person import data

def get_full_name(name, surname):
    return  f"User name: {name} {surname}"

def print_person():
    a = data.get_user["Name"]
    b = data.get_user["Surname"]
    print(get_full_name(a, b))