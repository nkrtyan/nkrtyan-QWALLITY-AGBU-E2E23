# with open('myfile.txt', 'a+') as file:
#     file.write("Hello")
#     file.write("\nit's my first file handling!")
#     file.seek(0)
#     mytext = file.read()
#     print(mytext)


letters = ["A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for i in letters:
    with open(i + '.txt', 'a+') as file:
        pass

print("Files was created")


