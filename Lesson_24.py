#Write a Python program to get the Fibonacci series between 0 to 50. 

a = 0
b = 1

while a < 50:
    print(a, end=" ")
    next_number = a + b
    a = b
    b = next_number

# Write a Python program that accepts a string and calculates the number of digits and letters.  


text = input ("abc12347e")

letters = 0
digits = 0

for character in text:
    if character.isalpha():
        letters += 1
    elif character.isdigit():
        digits += 1

print("Number of letters:", letters)
print("Number of digits:", digits)

# Write a Python program to print alphabet pattern 'L'  
# Expected Output:
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *****


# Couldnt do it