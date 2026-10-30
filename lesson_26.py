def file_open(filename):
    with open (filename, "a+", encoding="utf - 8") as file:
        file.write("Hello\n")
        file.write("it’s my first file handling!\n")
        file.seek(0)

        print(file.read())

file_open('my_file.txt')   

def generate_files():
    for i in range(ord('A'), ord('Z') + 1):
        letter = chr(i)
        filename = f"{letter}.txt"

        with open(filename, "w", encoding="utf-8") as file:
            file.write (f"{filename} file")
        
generate_files()        
  