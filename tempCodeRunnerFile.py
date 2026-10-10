name = input("Input your name: ")
age = int(input("Input your age: "))

decades = age // 10
units = age % 10

print(f"Hi {name}. My name is {name}, and I'm {age} years old. My age consists of {decades} decades and {units} units.")