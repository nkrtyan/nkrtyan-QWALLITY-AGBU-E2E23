
# Write a Python program which will open file, if not exist than create it.  
# Append the following text with two lines: 
# Hello –> first line
# it’s my first file handling! –> second line
# Read data from the file and print in the Terminal. 

# TODO, move the logic under function and give file name as an argument
with open('tatev.txt', 'a') as file:
    file.write('Hello')
    file.write('\nit’s my first file handling!')

with open('tatev.txt', 'r') as file: # TODO, code duplication, instead of opening file again use seek()0
    print(file.read())

# Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.

# TODO, create function and call it, logic is correct
for i in range(65,91):
    result = chr(i)
    with open(f'{result}.txt', 'x') as file:
        pass