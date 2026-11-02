import os

def write_and_read_file(file_name, text): # TODO, use with open, no need to close the file
    file = open(file_name, "a+")
    file.write(text)
    file.seek(0)
    file_text = file.read()
    print(file_text)
    file.close()

def create_alphabet_files(alphabet, folder):
    for letter in alphabet:
        file = open(folder + "/" + letter + ".txt", "w")
        file.close()

def delete_alphabet_files(alphabet, folder):
    for letter in alphabet:
        file_name = folder + "/" + letter + ".txt"

        if os.path.exists(file_name):
            os.remove(file_name)

def delete_file(file_name, folder): # TODO, need to use utills instead of 
    file_path = folder + "/" + file_name

    if os.path.exists(file_path):
        os.remove(file_path)
