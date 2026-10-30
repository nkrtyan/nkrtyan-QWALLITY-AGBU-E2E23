import data
def get_full_name(name, surname):
    return f"{name} {surname}"
# returned_info = get_full_name(data.my_info["name"], data.my_info["surname"])
# print(returned_info)

def print_person():
    returned_info = get_full_name(data.my_info["name"], data.my_info["surname"])
#     data.my_info.person_info = get_full_name(data.my_info["name"],data.my_info["surname"])
    print(returned_info)


# def print_person(get_full_name):
#        full_name = get_full_name(data.my_info["name"], data.my_info["surname"])