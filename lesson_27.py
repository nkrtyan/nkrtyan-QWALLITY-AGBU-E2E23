import os
import shutil

directory_name = 'Demo'

def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)

file_name = 'test.txt'
file_path = f'{directory_name}/{file_name}'
add_text = 'This is the content of the file.'

def write_file(file_path, add_text):
    with open(file_path , 'w') as file:
        file.write(add_text)



def read_file(file_path):
    with open(file_path, 'r') as file:
        print(file.read())

def delete_directory(directory_name):
    if os.path.exists(directory_name):
        question = input('Do you want to delete the "Demo" directory with all its files? (Yes/No): ')
        if question == 'Yes':
            shutil.rmtree(directory_name)
    else:
        print('This directory does not exist.')


if __name__ == "__main__":
    create_directory(directory_name)
    write_file(file_path, add_text)
    read_file(file_path)
    delete_directory(directory_name)