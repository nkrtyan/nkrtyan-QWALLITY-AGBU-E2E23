
# Write a Python program which will open file, if not exist than create it.  
# Append the following text with two lines: 
# Hello –> first line
# it’s my first file handling! –> second line
# Read data from the file and print in the Terminal. 

with open('tatev.txt', 'a') as file:
    file.write('Hello')
    file.write('\nit’s my first file handling!')

with open('tatev.txt', 'r') as file:
    print(file.read())

# Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.

for i in range(65,91):
    result = chr(i)
    with open(f'{result}.txt', 'x') as file:
        pass