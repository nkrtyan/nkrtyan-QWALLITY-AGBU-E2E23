#1. Write a Python program to get the Fibonacci series between 0 to 50.

a, b = 0, 1
while a <= 50:
    print (a, end = ' ')
    a, b = b, a + b
    
    
#2. Write a Python program that accepts a string and calculate the number of digits and letters.

text = "apple123"
letters = 0
digits = 0
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit ():
        digits += 1
print ("letters:", letters)
print ("digits:", digits)

# write a Python program to print alphabet pattern "L"

for i in range(7):
    print("*")
print ("*****")
  
  
  
#1. Write a Python program to get the Fibonacci series between 0 to 50.

a, b = 0, 1
while a <= 50:
    print (a, end = ' ')
    a, b = b, a + b
    
    
#2. Write a Python program that accepts a string and calculate the number of digits and letters.

text = "apple123"
letters = 0
digits = 0
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit ():
        digits += 1
print ("letters:", letters)
print ("digits:", digits)

# write a Python program to print alphabet pattern "L"

for i in range(7):
    print("*")
print ("*****")  