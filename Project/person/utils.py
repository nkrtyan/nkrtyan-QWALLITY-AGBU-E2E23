# fixed, this should contain data from data.py



def get_full_name(name, surname):
    return f"{name} {surname}"


def print_person(person):
    full_name = get_full_name(person["name"], person["surname"])
    print(full_name)