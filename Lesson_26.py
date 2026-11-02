with open("homework_26.txt", "w+", encoding="utf-8") as file: # TODO, move the logic inside the function and gioive filename as an argumnet
    file.write("Hello\n")
    file.write("it’s my first file handling!\n ")
    file.seek(0)
    data = file.read()
    print(data)


        
# TODO, the same here
for i in range(ord('A'), ord('Z') + 1):
    char = chr(i)
    with open(char + '.txt', 'w', encoding="utf-8") as file:
        file.write(char)
# Nel, the logic in both execrises are correct
  