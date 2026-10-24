# 1.	Write a Python program to get the Fibonacci series between 0 to 50. 

fib_sec = [0,1]
for i in range(1, 51):
    next_number = fib_sec[i] + fib_sec[i - 1]
    if next_number >= 50:
        break
    fib_sec.append(next_number)
print(f"The Fibonacci sequence between 0 to 50 in the list is. {fib_sec}")


# 2. Write a Python program that accepts a string and 
# calculates the number of digits and letters.  

str_py = "Python 3.13"
letter_count = 0
digits_count = 0
for i in range(len(str_py)):
    item = str_py[i]
    if item.isalpha():
        letter_count+=1
    elif item.isdigit():
        digits_count+=1
print(f"Lettrs in the string: {letter_count}\n Digits in the string: {digits_count}")

# 3.	Write a Python program to print alphabet pattern 'L'  

for i in range(7):
    if i == 6:
        print("*****")
    else:
        print("*")