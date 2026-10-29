from person.data import person

def get_full_name(name, surname):
    return name + " " + surname

def print_person():
    print(get_full_name("Full name is: ", get_full_name(person["name"], person["surname"]))) # TODO, you don\t need to call twice the function get_full_name, call once and pass name and surname
