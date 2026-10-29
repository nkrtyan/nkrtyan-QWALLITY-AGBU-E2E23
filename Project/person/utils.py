def get_full_name(name, surname):
    return (f"{name} {surname}")

# print(get_full_name("Anna", "Shamamyan"))

from person.data import person

def print_person():
    full_name = get_full_name(person['name'], person['surname'])
    print(full_name)



# print(get_full_name("Anna", "Shamamyan"))




