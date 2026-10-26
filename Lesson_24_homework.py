# # Write a Python program to get the Fibonacci series between 0 to 50.

numbers = [0, 1]

while numbers[-1] + numbers[-2] <= 50:
    numbers.append(numbers[-1] + numbers[-2])

print(f"Fibonacci series between 0 and 50: {numbers}")


# # Write a Python program that accepts a string and calculates the number of digits and letters.

text = input("Enter a string: ")

letters = 0
digits = 0

for i in text:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1

print("Letters", letters)
print("Digits", digits)

# Write a Python program to print alphabet pattern 'L'

height = int(input("Enter height: "))
width = int(input("Enter width: "))

i = 1

while i < height:
    print("*")
    i += 1

print("* " * width)
