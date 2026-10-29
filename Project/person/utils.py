from data import mydata
def get_full_name(name, surname):
    return name + " " + surname




def  print_person():
    print(get_full_name(mydata["name"], mydata["surname"]))


