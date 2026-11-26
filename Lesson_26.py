filename = "homework_26.txt"
content = "Hello\n"
content1 = "it’s my first file handling!\n "

def create_file(filename, content):
    with open(filename, "w+", encoding="utf-8") as file:
        file.write(content)
        file.seek(0)
        data = file.read()
        print(data)
with open(filename, "w+", encoding="utf-8") as file: # TODO, move the logic inside the function and gioive filename as an argumnet
    file.write(content)
    file.write(content1)
    file.seek(0)
    data = file.read()
    print(data)


        
# TODO, the same here
for i in range(ord('A'), ord('Z') + 1):
    char = chr(i)
    with open(char + '.txt', 'w', encoding="utf-8") as file:
        file.write(char)
# Nel, the logic in both execrises are correct
  