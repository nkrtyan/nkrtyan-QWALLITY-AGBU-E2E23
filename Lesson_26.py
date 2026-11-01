with open("homework_26.txt", "w+", encoding="utf-8") as file:
    file.write("Hello\n")
    file.write("it’s my first file handling!\n ")
    file.seek(0)
    data = file.read()
    print(data)


        

for i in range(ord('A'), ord('Z') + 1):
    char = chr(i)

    with open(char + '.txt', 'w', encoding="utf-8") as file:
        file.write(char)
  