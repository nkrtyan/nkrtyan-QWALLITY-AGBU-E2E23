name = input("Enter your name: ")
age = int(input("Enter your age: "))
if(age > 0 and age < 10):
    unit = age % 10
    print(f"Hello, my name is  {name}. My age is {age}, it is consists of {unit} units.") # TODO, the same line in 9, so need to combie
elif(age >= 10):
    decades = age // 10
    unit = age % 10
    print(f"Hello, my name is  {name}. My age is {age}, it is consists of {decades} decades and {unit} units")
else:
    print("Please enter a valid number!!")
# Nel, good with if else:) working code