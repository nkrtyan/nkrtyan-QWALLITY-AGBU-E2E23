# with open('myfile.txt', 'a+') as file: # TODO, make function and give file name as an argument
#     file.write("Hello")
#     file.write("\nit's my first file handling!")
#     file.seek(0)
#     mytext = file.read()
#     print(mytext)


letters = ["A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# TODO, no need keep seperate letters in the list just use "ABC..."
for i in letters:
    with open(i + '.txt', 'a+') as file:
        pass

print("Files was created")
# TODO, the logic always keep in the function as you have already learn it :)

