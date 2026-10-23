# Write a Python program to get the Fibonacci series between 0 to 50. 
a = 0 
b = 1
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b


# Write a Python program that accepts a string and calculates the number of digits and letters. 
sample_data = input("Enter a string: ")
digit_count = 0
letter_count = 0
for char in sample_data:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        letter_count += 1
print(f"Number of digits: {digit_count}")
print(f"Number of letters: {letter_count}")


# Write a Python program to print alphabet pattern 'L'
for i in range(7):
    for j in range(7):
        if j == 0 or i == 6:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
    
# Write a Python program to print alphabet pattern 'V'
for i in range(7):
    for j in range(13):
        if j == i or j == 12 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()