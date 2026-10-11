# Calculate the number of decades and remaining years from the user's age.

age = int(input("How old are you?\n"))

decades = age // 10
remainder = age % 10

# TODO, why you move print part to the next line? - fixed
print(f"Your age is {decades} decades and {remainder} year(s) old.")
# Nel, code is correct