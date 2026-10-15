name = input("Enter your name: ")
age = int(input("Enter your age: "))
if(age > 0):
    decades = age // 10
    unit = age % 10
    print(f"Hello, my name is  {name}. My age is {age}, it is consists of {decades} decades and {unit} units") # FIX
else:
    print("Please enter a valid number!!")
# Nel, good with if else:) working code