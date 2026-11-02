# TODO, create function an dfile name give as an argument
with open ("my_file.txt", "a+", encoding="utf-8") as my_file:
    line1 = "Hello!"
    line2 = "it’s my first file handling!"
    my_file.writelines([line1 + "\n", line2])
    my_file.seek(0)
    file_info = my_file.readlines()
    for i in file_info:
        print(i, end="")
# Nel, correct


# I have some issue with this code, can't find the generated files
# TODO, you need to call the function, you just declare it :)
def generate_files():
    for f in range(65, 91):
        file_name = chr(f)
        with open(f"{file_name}.txt", "w", encoding="utf-8"):
            continue
print("Files generated successfully.")
generate_files()
# Nel, code is correct