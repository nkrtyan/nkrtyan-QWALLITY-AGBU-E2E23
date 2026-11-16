# file = open("lesson26.txt", "a", encoding="utf-8")
# 
# file.write("Hello\n")
# file.write("it's my first file handling!\n")
# 
# file.close()
# 
# file = open("lesson26.txt", "r", encoding="utf-8")
# f = file.read()
# print(f)
# file.close()



# with open("lesson26.txt", "a", encoding="utf-8") as file:
    # file.write("Hello\n")
    # file.write("it’s my first file handling!\n")
# 
# with open("lesson26.txt", "r", encoding="utf-8") as file:
    # data = file.read()
    # print(data)


def print_letter_filenames():
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in alfabet:
        print(letter + ".txt")


print_letter_filenames()
        
