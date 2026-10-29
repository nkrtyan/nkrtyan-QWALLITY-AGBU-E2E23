from person.data import person

def get_full_name(name, surname):
    return name + " " + surname

# def print_person():
#     print("Full name is: ", get_full_name(person["name"], person["surname"])) # TODO, you don\t need to call twice the function get_full_name, call once and pass name and surname - fixed

def print_person(name, surname):
    print("Full name is: ", get_full_name(name, surname))
