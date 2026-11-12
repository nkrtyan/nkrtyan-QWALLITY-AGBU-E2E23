import os
direct_name="Direct"
file_name ="New_direct.txt"
content = "Hello team!"
def new_direct(direct_name, file_name,content): 
    if not os.path.exists(direct_name):
        os.mkdir(direct_name)
    os.chdir(direct_name)
    with open(file_name, "w+") as file:
        file.write(content)


new_direct(direct_name, file_name,content)

def delete_direct(direct_name):
    question = input("dO YOU WANT TO DELETE DIRECTION? YES OR NO:")
    if question =="YES":
        if os.path.exists(direct_name):
            shutil.rmtree(direct_name)

if __name__  == "__main__":
    new_direct(direct_name,file_name,content)
    delete_direct(direct_name)
