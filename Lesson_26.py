f = open("test.txt", "a+", encoding="utf-8")
f.write("Hello\n")
f.write("it's my first file handing!\n")
f.seek(0)
data = f.read()
print(data)
f.close()



#Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.
for i in range (26):
    file_name = chr(65 + i) + ".txt"
    f = open(file_name, "w", encoding="utf-8")
    f.write("this is file " + chr(65 + i) + "\n")
    f.close()
    
    