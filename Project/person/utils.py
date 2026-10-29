from . import data 


def get_full_name(person):
    return person['name'] + ' ' + person['surname']  #fix


def print_person(person):
    print(get_full_name(person))   #fix
    