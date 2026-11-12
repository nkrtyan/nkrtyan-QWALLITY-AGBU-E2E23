# file =open("data.txt", "w") # stexcum e jnjum e
# file.write("Hello\n")
# file.write("its my first fail handeling")
# file.close()
# file =open("data.txt","r") #stexcum e avelacnum e
# print(file.read())
# file.close()

def create_files():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in alphabet:
        file = open(letter + ".txt", "w")
        file.close()

create_files()