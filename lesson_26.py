
# Write a Python program which will open file, if not exist than create it.  
# Append the following text with two lines: 
# Hello –> first line
# it’s my first file handling! –> second line
# Read data from the file and print in the Terminal. 

title = 'tatev.txt'

def create_file(title):
    with open(title , 'a+') as file:
        file.write('Hello')
        file.write('\nit’s my first file handling!')

        file.seek(0)
        print(file.read())

create_file(title)


# Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.

def create_files():
    for i in range(65,91):
        result = chr(i)
        with open(f'{result}.txt', 'x') as file:
            pass
create_files()
